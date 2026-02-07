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
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/00098a80-5c47-4008-be00-cd6dd16099c9" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/db2de9dc-107b-456c-b8fc-24d58cf43424" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/fbcedf7d-bbd7-4811-9a12-0945bba372f2" />

<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/ae19c085-4da9-4c9e-afed-848c8c8f6d4d" />

