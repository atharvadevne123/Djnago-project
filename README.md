# 👥 Employee Management System API

A robust Django REST API for managing employees, departments, attendance tracking, and performance reviews. Built with PostgreSQL, JWT Authentication, and Swagger for seamless API exploration.

---

## 🚀 Features

- Django 4.x + Django REST Framework
- PostgreSQL integration via `django-environ`
- Token-based authentication using JWT (SimpleJWT)
- CRUD APIs for:
  - Employees
  - Departments
  - Attendance Records
  - Performance Reviews
- Filtering, Sorting, and Pagination
- Swagger/OpenAPI docs at `/swagger/`
- Database seeding using Faker
- (Optional) Chart.js-based analytics

---

## 🛠️ Project Structure
```
employee_project/
├── employees/
├── attendance/
├── employee_project/
├── templates/
├── manage.py
├── requirements.txt
├── .env.example
```
---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/employee-management-system.git
cd employee-management-system
```
2. Create and Activate a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Configure .env File
```
Create a .env file based on .env.example:

DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

⸻

🗃️ Database Setup

1. Make Migrations
```
python manage.py makemigrations
python manage.py migrate
```
2. Seed the Database
```
python manage.py seed_data
```
Creates 50 fake employees with attendance and performance history.

⸻

🔐 Authentication

Uses JWT Authentication via SimpleJWT.

Obtain Token:
```
POST /api/token/
```
Refresh Token:
```
POST /api/token/refresh/
```
Include token in headers:
```
Authorization: Bearer <your_token>
```

⸻

🧪 API Documentation

Interactive docs available at:
```
/swagger/
```


⸻
