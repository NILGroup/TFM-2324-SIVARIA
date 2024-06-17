from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from ..models import AppUser

'''
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = AppUser
        fields = ("first_name", "last_name", "email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = AppUser
        fields = ("first_name", "last_name", "email",)
'''

"""
    Formulario para crear nuevos usuarios. Incluye todos los campos requeridos
    y un campo de confirmación de contraseña.
    """
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomAppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ('email', 'first_name', 'last_name', 'phone', 'id_rol')

class CustomAppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser
        fields = ('email', 'first_name', 'last_name', 'phone', 'id_rol', 'is_active', 'is_staff', 'is_superuser')
