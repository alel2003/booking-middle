# Booking-API

**Booking-api** is a RESTful API project created for records. The project is developed using **Django**, **Django REST Framework**, **Redis**, **Docker** and **PostgreSQL** as the database.

## 🚀 Quick Start

Follow these steps to get up and running with the Base-API on your local machine.

### 1. Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/alel2003/booking-middle.git
cd booking-middle
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

### 3. Docker container launch

```bash
docker compose up -d --build
```

### 4. Database create migration

```bash
chmod +x migrate.sh
sudo ./migrate.sh
```

### 5. Create superuser admin

```bash
docker exec -it <id> shell
python3 manage.py createsuperuser
```

### 6. Running tests

```bash
docker compose exec web python manage.py test
```
