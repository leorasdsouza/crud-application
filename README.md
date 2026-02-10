# CRUD API Application using FastAPI and PostgreSQL

A CRUD API application built with FastAPI and PostgreSQL (Supabase).

## Features
- Full CRUD operations (Create, Read, Update, Delete)
- FastAPI with automatic API documentation (Swagger UI)
- PostgreSQL database hosted on Supabase
- SQLAlchemy ORM for database operations
- Environment variables for secure configuration
- RESTful API design

## Tech Stack
- Backend: FastAPI, Python 3.9+
- Database: PostgreSQL (Supabase)
- ORM: SQLAlchemy
- Validation: Pydantic

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/fintech-crud-internship.git
cd fintech-crud-internship
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv

Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a .env file in the root directory:
```bash
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@YOUR_SUPABASE_URL:5432/postgres
```

### 5. Run the Application
```bash
uvicorn main:app --reload
```
## API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/` | Welcome message |
| GET | `/items/` | List all items |
| POST | `/items/` | Create a new item |
| GET | `/items/{id}` | Get item by ID |
| PUT | `/items/{id}` | Update item |
| DELETE | `/items/{id}` | Delete item |

## API Documentation
Visit http://localhost:8000/docs for interactive API testing.

## 🗄 Database Schema
```bash
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(500)
);
```