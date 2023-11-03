# pyPlant
This project is a Django Project designed to help managing your plants (when to water them, when to repot & fertilize them, etc)
## Prerequisites
- **Python 3.9+**
- **Pipenv**
- **Redis** (`brew install redis`)
## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/valentindegrange/pyPlant.git
cd pyPlants
```
### 2. Install the dependencies
To install the dependencies for the project, run:
```bash
pipenv install
```
### 3. Activate Virtual Environment
Activate Pipenv virtual env:
```bash
pipenv shell
```
### 4. Database Setup
Setup the db (and optionally generate new migrations):
```bash
python manage.py makemigrations # optional
python manage.py migrate
```
### 5. Create an Admin User
To create a superuser, run:
```bash
python manage.py createsuperuser
```
Follow the prompts to setup username, email and password.
### 6. Run locally
To run the server & redis, run:
```bash
python manage.py runserver
```
In a new terminal window, run the redis server:
```bash
redis-server
```
In a new terminal window, run the celery beat worker:
```bash
python -m celery -A pyPlants beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
In a new terminal window, run the celery worker:
```bash
python -m celery -A pyPlants worker -l info
```

The application will be accessible at http://127.0.0.1:8000/. The admin interface can be accessed at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier.

