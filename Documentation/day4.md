# day4 -

🌐 Day 2: Django URLs & Views
🚦 Overview
How Django handles requests

Setting up routes (urls.py)

Writing views (views.py)

Using HttpResponse and render()

URL path converters

Project-level vs app-level routing

🔁 1. Django Request Flow (High Level)
Browser sends request: GET /about/

Django looks in urls.py to match the pattern

If matched, Django calls the view function tied to that URL

View returns a response (HTML, JSON, etc.)

Django sends that response back to the browser

🧩 2. URL Routing – urls.py
When you create a Django project, urls.py looks like this:

python# myproject/urls.py

from django.contrib import admin
from django.urls import path
from myapp import views # <-- Import your views

urlpatterns = [
path('admin/', admin.site.urls),
path('hello/', views.hello_world), # New route!
]
🧠 3. Views – views.py
Inside your app (e.g. myapp/views.py), define a simple view:

python# myapp/views.py

from django.http import HttpResponse

def hello_world(request):
return HttpResponse("Hello, Django learner!")
💡 Explanation:
request: A HttpRequest object

HttpResponse: Sends back plain text, HTML, etc.

🧱 4. render() – Return HTML templates
Create a templates/ folder inside your app:

arduinomyapp/
├── templates/
│ └── myapp/
│ └── home.html
home.html

html<!DOCTYPE html>

<html>
  <head><title>Welcome</title></head>
  <body>
    <h1>Hi, {{ name }}! Welcome to Django 🚀</h1>
  </body>
</html>
views.py

pythonfrom django.shortcuts import render

def home(request):
return render(request, 'myapp/home.html', {'name': 'Student'})
urls.py

pythonpath('', views.home, name='home'),
🔄 5. URL Path Converters
python# urls.py
path('greet/<str:username>/', views.greet_user)
python# views.py
def greet_user(request, username):
return HttpResponse(f"Hello, {username.capitalize()}!")
Built-in path converters:
Type Matches Example
str Non-empty string (default) /<str:name>/
int Integers /<int:year>/
slug Letters, numbers, hyphens /<slug:slug>/
uuid UUID strings /<uuid:id>/
path Like str, but can include slashes /<path:subpath>/

🛠 Best Practices
✅ Always name your routes:

pythonpath('hello/', views.hello_world, name='hello')
✅ Use reverse() or {% url %} in templates to avoid hardcoding URLs.

✅ Keep project-level routing (myproject/urls.py) clean. Include app routes like:
