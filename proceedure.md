## Basic procedure to make Django project and app up running
### Create Django project, in terminal, type 'django-admin startproject <project name> .
### Create App in project directory, in terminal, type 'python manage.py startapp <app name>
### Connect App to the project, go to project foldter, add app name to INSTALLED_APPs in settings.py
### To run the project, in terminal, type python manage.py runserver

<!-- Code database Model -->
### Go to app directory, open models.py file, define a class that inherits models.Model and register table items, with def __str__(self) and return statement
### run python manage.py makemigration
### run python manage.py migrate