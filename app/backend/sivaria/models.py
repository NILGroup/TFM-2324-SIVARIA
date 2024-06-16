from django.db import models
from django.contrib.auth.models import AbstractUser

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

class AppUser(models.Model): 
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'User: {self.name} {self.surname} - {self.email}'
    
class UserHasParent(models.Model):
    id_son = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    #id_parent_1 = models.ForeignKey(AppUser, on_delete=models.SET_NULL, allow_null=True)
    #id_parent_2 = models.ForeignKey(AppUser, on_delete=models.SET_NULL, allow_null=True)
    phone_parent_1 = models.CharField(max_length=15, null=True)
    phone_parent_2 = models.CharField(max_length=15, null=True)

    def __str__(self) -> str: 
        return f'UserHasParent: {self.id_son.id} - {self.id_son.name} {self.id_son.surname}'
