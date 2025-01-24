from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('ops', 'Operation User'),
        ('client', 'Client User'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    # Add related_name to resolve clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='client',
        blank=True,
        help_text='client',
        verbose_name='user permissions',
    )


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    allowed_types = ['pptx', 'docx', 'xlsx']

    def save(self, *args, **kwargs):
        if not self.file.name.split('.')[-1] in self.allowed_types:
            raise ValueError('Invalid file type. Allowed: pptx, docx, xlsx')
        super().save(*args, **kwargs)

class OTPVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, default=get_random_string(6, '0123456789'))
    is_verified = models.BooleanField(default=False)
