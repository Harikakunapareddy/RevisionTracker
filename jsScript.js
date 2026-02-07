const BASE_URL = "http://127.0.0.1:5000";
const userEmail = localStorage.getItem("userEmail");

/* AUTH GUARD */
if (location.pathname.includes("dashboard") && !userEmail) {
    location.href = "login.html";
}

/* LOGIN */
const loginForm = document.getElementById("loginForm");
if (loginForm) {
    loginForm.onsubmit = async e => {
        e.preventDefault();
        const res = await fetch(`${BASE_URL}/login`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                email: loginEmail.value,
                password: loginPassword.value
            })
        });

        if (res.ok) {
            localStorage.setItem("userEmail", loginEmail.value);
            location.href = "dashboard.html";
        } else {
            alert("Invalid credentials");
        }
    };
}

/* REGISTER */
const registerForm = document.getElementById("registerForm");
if (registerForm) {
    registerForm.onsubmit = async e => {
        e.preventDefault();
        const res = await fetch(`${BASE_URL}/register`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                username: username.value,
                email: email.value,
                password: password.value
            })
        });

        const data = await res.json();
        alert(data.message);
        if (res.ok) location.href = "login.html";
    };
}

/* LOGOUT */
const logoutBtn = document.getElementById("logoutBtn");
if (logoutBtn) {
    logoutBtn.onclick = () => {
        localStorage.clear();
        location.href = "login.html";
    };
}

/* DASHBOARD */
const taskForm = document.getElementById("taskForm");
const taskList = document.getElementById("taskList");
const generalNotes = document.getElementById("generalNotes");
const saveNotes = document.getElementById("saveNotes");

if (taskForm) {
    taskForm.onsubmit = e => {
        e.preventDefault();
        fetch(`${BASE_URL}/tasks`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ email: userEmail, task: taskInput.value })
        }).then(loadTasks);
        taskInput.value = "";
    };
}

function loadTasks() {
    fetch(`${BASE_URL}/tasks?email=${userEmail}`)
        .then(res => res.json())
        .then(data => {
            taskList.innerHTML = "";
            data.forEach(t => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td><input type="checkbox" ${t.completed ? "checked" : ""}></td>
                    <td>${t.task}</td>
                    <td><input type="checkbox" ${t.revision ? "checked" : ""}></td>
                    <td><button class="note-icon">📝</button></td>
                    <td><button class="delete-btn">❌</button></td>
                `;

                tr.querySelectorAll("input")[0].onchange = e =>
                    fetch(`${BASE_URL}/tasks/complete`, {
                        method: "POST",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({ index: t.id, completed: e.target.checked })
                    });

                tr.querySelectorAll("input")[1].onchange = e =>
                    fetch(`${BASE_URL}/tasks/revision`, {
                        method: "POST",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({ index: t.id, revision: e.target.checked })
                    });

                tr.querySelector(".delete-btn").onclick = () =>
                    fetch(`${BASE_URL}/tasks/delete`, {
                        method: "POST",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({ index: t.id })
                    }).then(loadTasks);

                tr.querySelector(".note-icon").onclick = () => {
    const notesSection = document.getElementById("notesSection");
    const notesBox = document.getElementById("generalNotes");

    // Scroll to notes section
    notesSection.scrollIntoView({ behavior: "smooth", block: "center" });

    // Put cursor inside textarea
    notesBox.focus();

    // Optional highlight (recommended)
    notesBox.style.border = "2px solid #007bff";
    setTimeout(() => {
        notesBox.style.border = "1px solid #ccc";
    }, 1200);
};


                taskList.appendChild(tr);
            });
        });
}

/* NOTES */
if (generalNotes && saveNotes && userEmail) {
    fetch(`${BASE_URL}/notes?email=${userEmail}`)
        .then(res => res.json())
        .then(data => generalNotes.value = data.notes || "");

    saveNotes.onclick = async () => {
        const res = await fetch(`${BASE_URL}/notes`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                email: userEmail,
                notes: generalNotes.value
            })
        });

        alert(res.ok ? "Notes saved successfully" : "Save failed");
    };
}

if (userEmail && taskList) loadTasks();
