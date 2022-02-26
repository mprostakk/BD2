# BD2 - Scooters (Bolt / Lime clone) 

This is a university project for BD2.
The documentation can be found in the docs/ folder.
The project was mainly focused on builing a db schema and implementing it in a relational database.

(Python 3.9.4)

## To run
- create venv
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`
- go to `localhost:8000/admin`


## To make new migration
- `python manage.py makemigrations`
- `python manage.py migrate`


## To use linter
- `black --line-length=100 .`
- `isort .`


## PG-Trigger
`https://django-pgtrigger.readthedocs.io/en/latest/index.html`

Triggers are added to database on migrate!
