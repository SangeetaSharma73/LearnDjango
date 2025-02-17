````markdown name=setup_login_register_with_tokens_in_django.md
# Setup Login and Register Functionality in Django using Tokens

## Step-by-Step Guide

### Step 1: Setup Django Project

1. **Create a new Django project** (if not already created):
    ```bash
    django-admin startproject myproject
    cd myproject
    ```

2. **Create a new Django app** for authentication:
    ```bash
    python manage.py startapp authapp
    ```

3. **Add the new app to `INSTALLED_APPS`** in `settings.py`:
    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'rest_framework.authtoken',
        'authapp',
    ]
    ```

### Step 2: Implement Token Authentication

1. **Install Django REST Framework** and its token authentication module:
    ```bash
    pip install djangorestframework
    pip install djangorestframework-simplejwt
    ```

2. **Configure Django REST Framework** in `settings.py`:
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
    }
    ```

3. **Create Django views** for user registration and login that return tokens:

    **views.py** in `authapp`:
    ```python name=authapp/views.py
    from rest_framework import status
    from rest_framework.response import Response
    from rest_framework.views import APIView
    from django.contrib.auth.models import User
    from rest_framework_simplejwt.tokens import RefreshToken
    from django.contrib.auth import authenticate

    class RegisterView(APIView):
        def post(self, request):
            username = request.data.get('username')
            password = request.data.get('password')
            if not username or not password:
                return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(username=username, password=password)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)

    class LoginView(APIView):
        def post(self, request):
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    ```

4. **Configure URL routing** to include the new authentication views:

    **urls.py** in `authapp`:
    ```python name=authapp/urls.py
    from django.urls import path
    from .views import RegisterView, LoginView

    urlpatterns = [
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='login'),
    ]
    ```

    **urls.py** in the project directory:
    ```python name=myproject/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('auth/', include('authapp.urls')),
    ]
    ```

5. **Add tests** to ensure authentication functionality works correctly:

    **tests.py** in `authapp`:
    ```python name=authapp/tests.py
    from django.test import TestCase
    from django.contrib.auth.models import User
    from rest_framework.test import APIClient

    class AuthTests(TestCase):
        def setUp(self):
            self.client = APIClient()

        def test_register(self):
            response = self.client.post('/auth/register/', {'username': 'testuser', 'password': 'testpass'})
            self.assertEqual(response.status_code, 201)
            self.assertIn('access', response.data)
            self.assertIn('refresh', response.data)

        def test_login(self):
            User.objects.create_user(username='testuser', password='testpass')
            response = self.client.post('/auth/login/', {'username': 'testuser', 'password': 'testpass'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('access', response.data)
            self.assertIn('refresh', response.data)
    ```

That's it! You have successfully set up login and registration functionality in Django using tokens. This setup allows users to register and log in, receiving JWT tokens for authentication. 🚀
````