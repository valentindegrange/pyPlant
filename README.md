# pyPlant
This project is a Django Project designed to help managing your plants (when to water them, when to repot & fertilize them, etc)  
Backend for [PlantWiz](https://github.com/valentindegrange/WizPlant)
## Prerequisites
- **Python 3.9+**
- **Pipenv**
- **Redis** (`brew install redis`)
## Installation & Setup
### Clone the Repository
```bash
git clone https://github.com/valentindegrange/pyPlant.git
cd pyPlants
```
### Install the dependencies
To install the dependencies for the project, run:
```bash
pipenv install
```
### Env Variables
Copy paste the `.env.template` file and rename it to `.env`

### (optional) Enable OpenAI
To enable OpenAI, get an OpenAI API key and paste it in the `.env` file:
```
OPENAI_API_KEY = "your_api_key"
```
### Activate Virtual Environment
Activate Pipenv virtual env:
```bash
pipenv shell
```
### Database Setup
Setup the db (and optionally generate new migrations):
```bash
python manage.py makemigrations # optional
python manage.py migrate
```
### Create an Admin User
To create a superuser, run:
```bash
python manage.py createsuperuser
```
Follow the prompts to setup username, email and password.
### Run locally
To run the server, run:
```bash
python manage.py runserver
```
  
Django admin: http://localhost:8000/admin  
API: http://localhost:8000/api/  

In a new terminal window, run the redis server:
```bash
redis-server
```
In a new terminal window, run the celery beat worker (here with an interval of 60s):
```bash
celery -A pyPlants beat -l debug --scheduler django_celery_beat.schedulers:DatabaseScheduler --max-interval=60
```
In a new terminal window, run the celery worker:
```bash
python -m celery -A pyPlants worker -l info
```
### 7. Seed the database
To seed the database with some data, run:
```bash
python manage.py gen_db
```
### 8. Testing
To run the tests, run:
```bash
python manage.py test
```
To check coverage, run:
```bash
coverage run --source='.' manage.py test
coverage report
```
### 9. API Authentication
The API is using a OAuth2 authentication system.  
The library used is [django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/index.html)

In order to use the API, you need to create an application in the Django admin. Some extra params for the Application:
- Authorization grant type: Authorization code
- Client type: Confidential
- Redirect uris: http://localhost:3000/oauth/callback https://oauth.pstmn.io/v1/callback
- Algorithm: No OIDC support  

Additional details are available in the [django-oauth-toolkit DRF documentation](https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html)  
### Postman Auth
In order to connect to the API using Postman, you need to do it in 2 steps (for now):
- Setup OAuth 2 Auth in Postman (with all the right params)
- Generate a new token (enter the superuser creds)
- Kill
- Generate a token again (your user will be already authenticated)
- Use the token

It's clanky, but we'll fix it later.
