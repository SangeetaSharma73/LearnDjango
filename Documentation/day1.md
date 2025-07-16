Day 1: Introduction to Django, covering:

✅ What is Django

✅ Django Project Structure

✅ Virtual Environments, pip, django-admin, manage.py

✅ settings.py and environment handling (dev vs prod)

I’ll walk you through like a mentor, with real-world context, examples, and tips.

🧠 1. What is Django?
Django is a powerful, batteries-included web framework written in Python. It’s used to build web apps quickly and securely — from blogs to enterprise-level systems.

🔧 Why Django?
Fast development (CRUD in minutes)

ORM: No need to write raw SQL

Admin interface: Auto-generated admin dashboard

Security: CSRF, XSS, SQL injection protection built-in

Scalable: Used by Instagram, Disqus, Mozilla, etc.

🧰 2. Django Project Structure
When you create a Django project, you'll see something like this:

markdown

myproject/
├── manage.py
├── myproject/
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
🔍 Explanation:
File/Folder Purpose
manage.py CLI tool to run the server, manage DB, etc.
myproject/ The main project folder (same name as your project)
**init**.py Python file to mark this folder as a package
settings.py Configuration for the project (DB, installed apps, etc.)
urls.py Global URL routes for the project
asgi.py / wsgi.py Entry points for asynchronous/synchronous web servers (for deployment)

💡 3. Virtual Environments, pip, django-admin, manage.py
✅ 3.1 Virtual Environment
Create isolated Python environments per project.

bash

python -m venv env # Create virtual environment
source env/bin/activate # Activate (Linux/Mac)
env\Scripts\activate # Activate (Windows)
✅ 3.2 Installing Django
bash

pip install django
Check version:

bash

django-admin --version
✅ 3.3 Creating a Project
bash

django-admin startproject myproject
cd myproject
python manage.py runserver
Visit: http://127.0.0.1:8000 – you’ll see the welcome page.

⚙️ 4. settings.py and Environments (dev vs prod)
The settings.py file holds all configuration for your Django project.

Important parts:
python

DEBUG = True # Set False in production
ALLOWED_HOSTS = ['*'] # Change to your domain/IP in prod
INSTALLED_APPS = [...] # Django + your apps
DATABASES = {...} # DB config (default is SQLite)
STATIC_URL = '/static/' # Static files like CSS
🔒 Dev vs Prod: Best Practices
✅ Development (settings_dev.py):

python

DEBUG = True
ALLOWED_HOSTS = []
✅ Production (settings_prod.py):

python

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
Then, in your project’s root settings.py:

python

import os
ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
from .settings*prod import *
else:
from .settings*dev import *
Use .env file + python-decouple or django-environ to manage sensitive settings.

🔨 Your Mini Assignment
✅ Create a new folder called djangolearn, then inside:

bash

python -m venv env
source env/bin/activate
pip install django
django-admin startproject myproject
cd myproject
python manage.py runserver
✅ Open myproject/settings.py and explore:

Change timezone and language

Add comments to understand sections

✅ Research: What is the difference between ASGI and WSGI?

✅ What’s Next?
Tomorrow, we’ll dive into URLs and Views:

How Django routes HTTP requests

Function-based views

HttpResponse and render()
