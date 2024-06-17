from django.db import models
from django.contrib.auth.models import AbstractUser
from .api.managers.managers import AppUserManager

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
    phone = models.CharField(max_length=20, unique=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'  # Establece el campo de email para la autenticación
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AppUserManager()

    def __str__(self) -> str:
        return f'User: {self.first_name} {self.last_name} - {self.email}'
    
class UserHasParent(models.Model):
    id_son = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    #id_parent_1 = models.ForeignKey(AppUser, on_delete=models.SET_NULL, allow_null=True)
    #id_parent_2 = models.ForeignKey(AppUser, on_delete=models.SET_NULL, allow_null=True)
    phone_parent_1 = models.CharField(max_length=15, null=True)
    phone_parent_2 = models.CharField(max_length=15, null=True)

    def __str__(self) -> str: 
        return f'UserHasParent: {self.id_son.id} - {self.id_son.name} {self.id_son.surname}'
