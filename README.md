# Base-API

**Base-api** is a RESTful API project created for use by underlying configurations. The project is developed using **Django**, **Django REST Framework** and **PostgreSQL** as the database.

## 🚀 Quick Start

Follow these steps to get up and running with the Base-API on your local machine.

### 1. Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/your-repo/Base-api.git
cd book-api
```

### 2. Create a virtual environment

```bash
python3 -m venv env
# Activate the environment (Linux/Mac)
source env/bin/activate
# Activate on Windows
env\Scripts\activate
```

### 3. Once activated, install the required dependencies listed in requirements.txt

```bash
pip install -r requirements.txt
```

### 3. Create a PostgreSQL Database and User

```bash
sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```

### 4. Apply Database Migrations

```bash
python3 manage.py migrate
```

### 5. Create a Superuser

```bash
python3 manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python3 manage.py runserver
```
