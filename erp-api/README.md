📘 ERP System API (FastAPI + SQLite)

A simple ERP System API built with FastAPI and SQLite, supporting Role-Based Access Control (RBAC) with three roles:

👑 Admin: Can create teacher/student accounts and view all tasks.

👩‍🏫 Teacher: Can create tasks for students and view only their tasks.

🎓 Student: Can view tasks assigned to them and update task status.

🚀 Features

✅ JWT-based Authentication & Authorization

✅ Role-based Permissions

✅ Task Management (CRUD with restrictions)

✅ SQLite Database (lightweight, auto-created)

✅ Swagger UI (/docs) & Redoc (/redoc)

📂 Project Structure
erp-system-api/
│-- main.py                # Entry point of FastAPI app
│-- database.py            # SQLite database setup
│-- models.py              # SQLAlchemy models
│-- schemas.py             # Pydantic schemas
│-- auth.py                # Authentication & JWT handling
│-- crud.py                # Database CRUD operations
│-- requirements.txt       # Dependencies
│-- README.md              # Project documentation

🛠️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/erp-system-api.git
cd erp-system-api

2️⃣ Create & activate virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the server
uvicorn main:app --reload


Server will start at:
👉 http://127.0.0.1:8000

🔑 Authentication Flow

Register User (by Admin) → /register

Role: admin / teacher / student

Login User → /login

Returns JWT Token

Use JWT in Headers

Authorization: Bearer <your_token_here>

📌 API Endpoints
🔹 Authentication

POST /register → Register new user (Admin only)

POST /login → Login & get JWT token

🔹 Tasks

POST /tasks/ → Teacher creates task for student

GET /tasks/ →

Admin: view all tasks

Teacher: view own created tasks

Student: view assigned tasks

PUT /tasks/{task_id} → Student updates task status

DELETE /tasks/{task_id} → Admin/Teacher delete task

🧪 Example Usage (Swagger UI)

Open 👉 http://127.0.0.1:8000/docs

Register an Admin account first.

Login as Admin, copy JWT token.

Use Authorize button in Swagger UI → Paste Bearer <token>.

Now you can create Teachers/Students and manage tasks.

📊 Example To-Do Workflow

Admin registers Teacher + Student

Teacher creates a new task for Student

Student views task & updates status (e.g., "Completed")

Admin monitors all tasks

✅ Requirements

Python 3.9+

FastAPI

Uvicorn

SQLAlchemy

Passlib (password hashing)

PyJWT (JWT Authentication)

Install with:

pip install fastapi uvicorn sqlalchemy passlib[bcrypt] pyjwt
