# helplineApp

## Description

This is an application for reporting defilement incidences through sms.
* Victims should be able to report an incidence through sending sms alert to the system
* The organization should be able to get a notification of the report sent by the victim
* The organization should be able to open a new case for the victim
* The organization should be able to update the case as it proceeds

## Requirements
* Python 3.7
* africa's talking
* postman
* pip
* virtualenv

# Installation
### 1)Clone the repo from GitHub:
$ git clone https://github.com/Ahmedsebit/helplineApp.git

### 2) Create a virtual environment and install the necessary packages with:
$ virtualenv -p python3 env

### 3) Activate virtual environment:
$ source env/bin/activate

### 4) cd to the root of the api:
$ cd helplineApp

### 5) Install requirements:
$ pip install -r requirements.txt

### 6) Make migrations:
$ python manage.py makemigrations
$ python manage.py migrate

### 8)Create Super User
$ python manage.py createsuperuser

### 7)Add the environment variables
$ export AFRICAS_TALKING_USERNAME = "THE USERNAME"
$ export AFRICAS_TALKING_API_KEY=“THEAPI_KEY"
$ export LAST_RECEIVED=0

# Runserver
$ python manage.py runserver

# Authentication
### Getting the token
The /api-token-auth/ is the authentication endpoint, which will be http://127.0.0.1:8000/api-token-auth/ from local server. The token is retrieved by submitting the username and password

### Using the token
The token is used in all the endpoints by adding the JWT+ token in the authorization header. Alternatively, the user can log in using the login links from the web application and the token will be generated, stored and refreshed by the application

# Accesing the application
The application can be accesed by using postman or for a better experience, using the web app.

# Users
Users include staff(superusers) and Normal Users
# Staff (superuser)
#### Are created using the command
$ python manage.py createsuperusers
#### Functions the supers users can do
| Funcion                                 | Request| command                 |
| ------------------------------------------ | -------| ------------------------|
| `/api-token-auth/`                         |`POST`  | Login and retrieve token|
| `/api/victims/create/`                      |`POST`  | Create Victims           |
| `/api/victims/`                             |`GET`   | GET All Victims         |
| `/api/victims/<victim_id>/`                 |`GET`   | GET Victims Detail       |
| `/api/victims/<victim_id>/update`           |`PUT`   | Update Victims Details  |
| `/api/victims/<victims_id>/delete`           |`DELETE`| DELETE Victims          |
| `/api/perpetrators/create/`                        |`POST`  | Create Perpetrator           |
| `/api/perpetrators/`                               |`GET`   | GET All Perpetrators         |
| `/api/perpetrators/<perpetrators_id>/`                     |`GET`   | GET Perpetrator Detail       |
| `/api/perpetrators/<serpetrators_id>/update`                   |`PUT`   | Update Perpetrator Details  |
| `/api/perpetrators/<erpetrators_id>/delete`                   |`DELETE`| DELETE Perpetrator          |
| `/api/reports/create/`           |`POST`  | Create Report          |
| `/api/reports/<report_id>/`              |`GET`   | GET Report Details     |
| `/api/reports/<report_id>/update`        |`PUT`   | Update Report Details  |
| `/api/reports/<report_id>/`              |`DELETE`| DELETE Reports          |
| `/api/cases/`                           |`GET`   | GET All Cases        |
| `/api/cases/create/`                   |`POST`   | CREATE Case    |
| `/api/cases/<case_id>/`               |`GET`   | GET Case Details     |
| `/api/Cases/<case_id>/update`        |`PUT`   | Update Case Details  |
| `/api/Cases/<case_id>/`              |`DELETE`| DELETE Case          |
| `/api/users/`                           |`GET`   | GET All Cases        |
| `/api/users/create/`                   |`POST`   | CREATE Case    |
| `/api/users/<user_id>/`               |`GET`   | GET Case Details     |
| `/api/Users/<user_id>/update`        |`PUT`   | Update User Details  |
| `/api/Users/<user_id>/`              |`DELETE`| DELETE User          |

# Running the tests
 $ python manage.py test --with-coverage
