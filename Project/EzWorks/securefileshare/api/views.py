from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User, UploadedFile, OTPVerification
from .serializers import UserSerializer, UploadedFileSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from cryptography.fernet import Fernet

# Encryption Key for URLs
ENCRYPTION_KEY = Fernet.generate_key()
cipher = Fernet(ENCRYPTION_KEY)

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user.user_type == 'client':
                otp = OTPVerification.objects.get(user=user).otp
                send_mail(
                    'Verify Your Email',
                    f'Your OTP is: {otp}',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                )
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmailView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        try:
            user = User.objects.get(email=email)
            otp_obj = OTPVerification.objects.get(user=user)
            if otp_obj.otp == otp:
                otp_obj.is_verified = True
                otp_obj.save()
                return Response({'message': 'Email verified successfully!'})
            return Response({'message': 'Invalid OTP!'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'message': 'Login successful!'})
        return Response({'message': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)

class FileUploadView(APIView):
    def post(self, request):
        if request.user.user_type != 'ops':
            return Response({'message': 'Permission denied!'}, status=status.HTTP_403_FORBIDDEN)
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'File uploaded successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DownloadFileView(APIView):
    def get(self, request, file_id):
        try:
            file = UploadedFile.objects.get(id=file_id)
            if request.user.user_type != 'client':
                return Response({'message': 'Permission denied!'}, status=status.HTTP_403_FORBIDDEN)
            encrypted_url = cipher.encrypt(str(file.id).encode()).decode()
            return Response({'download-link': f'/download-file/{encrypted_url}', 'message': 'success'})
        except UploadedFile.DoesNotExist:
            return Response({'message': 'File not found!'}, status=status.HTTP_404_NOT_FOUND)
