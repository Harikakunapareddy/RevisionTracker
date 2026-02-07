## 🚀 Project Overview

Revision Tracker is a full-stack web application that helps users manage their study topics, track revision status, and store important notes for interview preparation.
Users can add topics they study, mark them for revision when needed, and save key points to revise before interviews.

## 🎯 Problem Statement
While preparing for interviews, students often forget:
 - Which topics they have already studied
 - Which topics need revision
 - Important points to revise before interviews
This application provides a structured way to track studied topics, revision status, and important notes in one place.

## 🛠 Tech Stack
### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite

### Tools
- VS Code

## ⚙️Features
### User Authentication
- User registration
- Login validation
- Logout functionality

### Topic & Status Managemnet
- Add topics for studying
- Update topic status :
  - Studied
  - Marked for Revision
- View all topics in a dashboard

### Revision Notes

- Add important notes
- Store notes persistently
- Review notes before interviews

## Project Structure
```bash
revisionTracker/
│
├── Frontend/
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── styles.css
│ └── jsScript.js
│
├── backend/
│ ├── app.py
│ └── revision.db
│
├── api_endpoints.txt
├── db_schema.txt
└── README.md
```
## 🔗 REST API Endpoints

### 🔐 Authentication APIs

| Method | Endpoint | Description |
|------|--------|------------|
| POST | `/register` | Register new user |
| POST | `/login` | Authenticate user |
| GET | `/logout` | Logout user |

---

### 📘 Topic & Notes APIs

| Method | Endpoint | Description |
|------|--------|------------|
| POST | `/add_revision` | Add studied topic |
| GET | `/get_revisions` | Fetch user topics |
| POST | `/tasks/delete`     | Delete a topic 
| POST | `/add_notes` | Add revision notes |

## 🗄 Database Schema

### Users Table
- **id** – INTEGER (Primary Key)
- **username** – TEXT
- **password** – TEXT

### Topics Table
- **id** – INTEGER (Primary Key)
- **user_id** – INTEGER (Foreign Key)
- **topic** – TEXT
- **status** – TEXT
- **notes** – TEXT

<img width="1920" height="1200" alt="login" src="https://github.com/user-attachments/assets/0c81be4a-c089-45c3-b8fc-d65c2ab92ef5" />
<img width="1920" height="1200" alt="register" src="https://github.com/user-attachments/assets/1fb3adf5-4aea-49e3-8db0-e733175b3c02" />

<img width="1920" height="1200" alt="dashboard1" src="https://github.com/user-attachments/assets/cfae39f2-84fc-427e-96e5-64246e9e6e86" />
<img width="1920" height="1200" alt="dashboard2" src="https://github.com/user-attachments/assets/01dc0aa1-a519-4184-85e6-7e445a4511d3" />

## How to Run the Project
### Clone the Repository
```bash
git clone <your-github-repo-link>
cd revisionTracker

###Install Dependencies
pip install flask

### Run the Application
python backend/app.py

-------








