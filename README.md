# Django Local Library Notes

## Conda Environment Basics

```diff
# See all conda virtual environments
conda env list

# Enter a virtual environment
activate <env-name>

# Exit a virtual environment
conda deactivate
```

## Create Conda Environment

```diff
# Create a virtual environment with lastest version of Python
conda create -n <env-name> python

# Create a virtual environment with specific version of Python
conda create -n <env-name> python=3
conda create -n <env-name> python=3.8

# Create a virtual environment with Anaconda
conda create -n <env-name> anaconda
```

## Checkout Packages

```diff
# Check out Conda version
conda -V

# Check out Python version
python -V

# See all installed packages
conda list
```

## Remove Conda Environment/Package

```diff
# Remove a virtual environment
conda env remove -n <env-name>

# Remove packages in current environment
conda remove <package-name>
conda remove <package-name-1> <package-name-2>

# Remove a package in a virtual environment
conda remove -n <env-name> <package-name>
```

## Django - Create Project

```diff
# Install Django
python -m pip install django

# Check out Django version
pip freeze
python -m django version

# Create a Django Project
django-admin startproject <project-name>
```

## Django - Run Server In Local Machine

```diff
# Apply Migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser
# Enter the username of the superuser
# Enter the email of the superuser
# Enter the password of the superuser
# Enter the password again

# Run server (Django Admin: localhost:8000/admin)
python manage.py runserver
```

## Allow other computers to access the server

```diff
# Set ALLOWED_HOSTS in settings.py
ALLOWED_HOSTS = ['*']

# Run server (Django Admin: <xxx.xxx.xxx.xxx>:8000/admin)
python manage.py runserver 0.0.0.0:8000
```

## Django - Create an application

```diff
# Create an application
python manage.py startapp <app-name>

# Register an application in settings.py
INSTALLED_APPS = [
  ...
  'catalog',
]

# Hook up the URL mapper in urls.py
from django.urls import path
from django.urls import include
...
urlpatterns = [
  ...
  path('catalog/', include('catalog.urls')),
]

```









## Django - Other Project Settings in settings.py

```diff
# Time Zone
TIME_ZONE = 'Asia/Taipei'
```
