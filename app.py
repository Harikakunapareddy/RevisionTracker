from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "revision.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            notes TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            task TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            revision INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

init_db()

@app.after_request
def cors(res):
    res.headers["Access-Control-Allow-Origin"] = "*"
    res.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    res.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return res

@app.route("/")
def home():
    return "Revision Tracker Backend Running"

# ---------- REGISTER ----------
@app.route("/register", methods=["POST", "OPTIONS"])
def register():
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json(force=True)
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (data["username"], data["email"], data["password"])
        )
        conn.commit()
        return jsonify({"message": "Registration successful"}), 200
    except sqlite3.IntegrityError:
        return jsonify({"message": "User already exists"}), 400
    finally:
        conn.close()

# ---------- LOGIN ----------
@app.route("/login", methods=["POST", "OPTIONS"])
def login():
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json(force=True)
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (data["email"], data["password"])
    )
    user = cur.fetchone()
    conn.close()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"}), 200

# ---------- TASKS ----------
@app.route("/tasks", methods=["GET", "POST", "OPTIONS"])
def tasks():
    if request.method == "OPTIONS":
        return "", 200

    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        data = request.get_json(force=True)
        cur.execute(
            "INSERT INTO tasks (email, task) VALUES (?, ?)",
            (data["email"], data["task"])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Task added"}), 200

    email = request.args.get("email")
    cur.execute("SELECT * FROM tasks WHERE email=?", (email,))
    rows = cur.fetchall()
    conn.close()

    return jsonify([{
        "id": r["id"],
        "task": r["task"],
        "completed": bool(r["completed"]),
        "revision": bool(r["revision"])
    } for r in rows])

@app.route("/tasks/complete", methods=["POST", "OPTIONS"])
def complete_task():
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json(force=True)
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tasks SET completed=? WHERE id=?",
        (int(data["completed"]), data["index"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Updated"})

@app.route("/tasks/revision", methods=["POST", "OPTIONS"])
def revision_task():
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json(force=True)
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tasks SET revision=? WHERE id=?",
        (int(data["revision"]), data["index"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Updated"})

@app.route("/tasks/delete", methods=["POST", "OPTIONS"])
def delete_task():
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json(force=True)
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (data["index"],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})

# ---------- NOTES ----------
@app.route("/notes", methods=["GET", "POST", "OPTIONS"])
def notes():
    if request.method == "OPTIONS":
        return "", 200

    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        data = request.get_json(force=True)
        cur.execute(
            "UPDATE users SET notes=? WHERE email=?",
            (data["notes"], data["email"])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Notes saved"}), 200

    email = request.args.get("email")
    cur.execute("SELECT notes FROM users WHERE email=?", (email,))
    row = cur.fetchone()
    conn.close()

    return jsonify({"notes": row["notes"] if row else ""})

if __name__ == "__main__":
    app.run(debug=True)
