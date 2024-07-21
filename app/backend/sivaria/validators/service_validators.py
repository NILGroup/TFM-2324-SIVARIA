import re
from django.core.exceptions import ValidationError as CoreValidationError
from django.utils.translation import gettext as _
from rest_framework.serializers import ValidationError as SerializerValidationError

class UserValidator:
    def validate_email(self, email):
        if not email or not email.strip():
            raise CoreValidationError('Email vacío')
        return True

    def validate_username(self, username):
        if not username or not username.strip():
            raise CoreValidationError('Nombre de usuario vacío')
        return True

    def validate_password(self, password):
        if not password or not password.strip():
            raise CoreValidationError('Contraseña vacía')
        return True

        
    def validate_password(self, password):
        if not password or not password.strip():
            raise CoreValidationError('Contraseña vacía')
        return True
        
    def validate_first_name(self, first_name):
        if not first_name or not first_name.strip():
            raise CoreValidationError('Nombre vacío')
        return True
    
    def validate_last_name(self, last_name):
        if not last_name or not last_name.strip():
            raise CoreValidationError('Apellidos vacío')
        return True
    
    def validate_rol(self, rol):
        if not rol or not rol.strip():
            raise CoreValidationError('Rol vacío')
        '''
        # Check the password length
        if len(password) < 8:
            raise CoreValidationError("Tu contraseña debe tener una longitud de 8 caracteres")

        # Check if the password is entirely numeric
        if password.isdigit():
            raise CoreValidationError("Tu contraseña no debe ser completamente numérica.")

        # Check for at least one lowercase letter
        if not re.search(r'[a-z]', password):
            raise CoreValidationError("Tu contraseña debe contener al menos una minúscula.")

        # Check for at least one uppercase letter
        if not re.search(r'[A-Z]', password):
            raise CoreValidationError("Tu contraseña debe contener al menos una mayúscula.")

        # Check for at least one special character
        if not re.search(r'[\W_]', password):
            raise CoreValidationError("Tu contraseña debe contener al menos un caracter especial.")
        '''
        return True