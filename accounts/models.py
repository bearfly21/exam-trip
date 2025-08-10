import uuid
from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_email_confirmed = models.BooleanField(default=False)

    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class Token(models.Model):
    token = models.UUIDField(default=uuid.uuid4,unique=True)
    user = models.OneToOneField(CustomUser,  on_delete=models.CASCADE)
    created_at = models.DateField(  auto_now_add=True)