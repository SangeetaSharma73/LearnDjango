from django.urls import path
from .views import SignUpView, VerifyEmailView, LoginView, FileUploadView, DownloadFileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload-file/', FileUploadView.as_view(), name='upload-file'),
    path('download-file/<str:file_id>/', DownloadFileView.as_view(), name='download-file'),
]
