# FastAPI Social Backend
---
A robust, production-ready RESTful API built with FastAPI and PostgreSQL. This project serves as the backend engine for a social platform, featuring secure user authentication, database ORM integration, and relationship mapping between users and their content.

## What I've Built & Learned (So Far)

- **CRUD Operations:** Coded complete `GET`, `POST`, `PUT`, and `DELETE` routes to manage data dynamically.
- **Data Validation (Pydantic):** Implemented strict data schemas using `BaseModel` to validate client requests.
- **Error Handling:** Integrated `HTTPException` and explicit status codes (`201 Created`, `204 No Content`, `404 Not Found`) to prevent server crashes on edge cases.
- **Relational Database Architecture:** Migrated from in-memory structures to a robust PostgreSQL database using the SQLAlchemy ORM.
- **Secure Authentication & Authorization:** Implemented stateless authentication using JSON Web Tokens (JWT) and OAuth2PasswordBearer to protect specific API routes.
- **Data Security:** Integrated `passlib` and `bcrypt` algorithms for secure, one-way password hashing before storing credentials.
- **Advanced Data Validation:** Utilized Pydantic v2 (`pydantic-settings`) for strict schema validation, response modeling, and secure environment variable management.
- **Relational Mapping:** Built fully functional users and posts endpoints with Foreign Key constraints to ensure data integrity and track post ownership.
- **Database Version Control:** Integrated Alembic to track and manage database schema changes, ensuring smooth and predictable production deployments.
- **Automated Testing Architecture:** Built a comprehensive integration testing suite using Pytest, featuring dedicated testing databases, custom fixtures, and API client simulation to ensure 100% endpoint reliability.
- **CI/CD & Cloud Deployment:** Engineered an automated GitHub Actions pipeline to run Pytest suites on every push, containerized the application using Docker, and successfully deployed the live database and web service to the cloud.

## Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Security:** JWT (`python-jose`) & `passlib`
- **Configuration:** Pydantic-Settings
- **Testing:** Pytest
- **DevOps:** Docker, GitHub Actions, Render Cloud
- **Server:** Uvicorn (ASGI)

---

## How to Run This Locally

Follow these steps to set up and run the backend on your local machine.

---

### 1. Clone the Repository

```bash
git clone [https://github.com/mihirkamat03/FastAPI-Social-Backend.git](https://github.com/mihirkamat03/FastAPI-Social-Backend.git)
cd FastAPI-Social-Backend
```

---

### 2. Create & Activate Virtual Environment

#### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy psycopg2 passlib[bcrypt] python-jose pydantic-settings alembic pytest
```
---

### 4. Environment Variables Setup

```env
DATABASE_HOSTNAME=(YOUR DATABASE HOSTNAME)
DATABASE_PORT=5432
DATABASE_PASSWORD=(YOUR DATABASE PASSWORD)
DATABASE_NAME=(YOUR DATABASE NAME)
DATABASE_USERNAME=(YOUR DATABASE USERNAME)
SECRET_KEY=(YOUR SECRET KEY)
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 5. Run the Development Server

```bash
uvicorn main:app --reload
```
---
### About me-

Owner: Mihir Kamat

Role: Backend Engineer

Email: kamatmihir.cse@gmail.com

LinkedIn: https://www.linkedin.com/in/mihirkamat/

Portfolio: https://mihirkamat03.github.io/portfolio/
