# Task Manager API 🚀

A production-ready REST API for managing tasks, built with FastAPI and PostgreSQL.

## 🔗 Live Demo
- **API Base URL:** https://task-manager-api-xcds.onrender.com
- **Swagger UI (Docs):** https://task-manager-api-xcds.onrender.com/docs

## 🛠️ Tech Stack
- **Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** psycopg2
- **Deployment:** Render

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks/ | Get all tasks |
| POST | /tasks/ | Create a new task |
| GET | /tasks/{id} | Get a specific task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## ⚙️ Run Locally

```bash
# Clone the repo
git clone https://github.com/SravanKumarMekala/task-manager-api.git
cd task-manager-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add .env file
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taskdb

# Run the server
uvicorn main:app --reload
```

## 📂 Project Structure
```
task-manager-api/
├── routers/
│   └── tasks.py
├── database.py
├── schemas.py
├── main.py
└── requirements.txt
```