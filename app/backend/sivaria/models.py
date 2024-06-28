from django.db import models
from django.contrib.auth.models import AbstractUser
from .api.managers.managers import AppUserManager
from .validators.validators import SpanishPhoneValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self) -> str:
        return f"Post: {self.title}"
    

class Rol(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self) -> str:
        return f'Rol: {self.slug}'

class AppUser(AbstractUser): 
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    #In production, phone must be unique
    phone = models.CharField(max_length=9, null=True, validators=[SpanishPhoneValidator()], help_text='The phone number must contain only digits and must be a Spanish number.')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    # In production, the token must be unique and cannot be null
    expo_token = models.CharField(max_length=200, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'  # Establece el campo de email para la autenticación
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AppUserManager()

    def __str__(self) -> str:
        return f'User: {self.first_name} {self.last_name} - {self.email}'
    
class UserHasParent(models.Model):
    son = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    #id_parent_1 = models.ForeignKey(AppUser, on_delete=models.SET_NULL, allow_null=True)
    #id_parent_2 = models.ForeignKey(AppUser, on_delete=models.SET_NULL, allow_null=True)
    email_parent_1 = models.EmailField(unique=True, null=True, default=None)
    email_parent_2 = models.EmailField(unique=True, null=True, default=None)

    def __str__(self) -> str: 
        return f'UserHasParent: {self.son.id} - {self.son.first_name} {self.son.last_name}'

class PushNotificationType(models.Model):
    slug = models.CharField(max_length=20, unique=True, null=False)
    title = models.TextField(max_length=50)
    body = models.TextField(max_length=255)
    data = models.TextField(max_length=255, null=True, default=None, blank=True)

    def __str__(self) -> str:
        return f'PushNotificationType: {self.slug}'
