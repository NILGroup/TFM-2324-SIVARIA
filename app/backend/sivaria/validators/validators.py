# sivaria/validators.py
import re
from django.core.exceptions import ValidationError as CoreValidationError
from django.utils.translation import gettext as _
from rest_framework.serializers import ValidationError as SerializerValidationError

class SpecialCharacterPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Z]', password):
            raise CoreValidationError(
                _("Your password must contain at least one upper case letter."),
                code='password_no_upper',
            )
        if not re.search(r'[a-z]', password):
            raise CoreValidationError(
                _("Your password must contain at least one lower case letter."),
                code='password_no_lower',
            )
        if not re.search(r'[\W_]', password):  # \W busca cualquier carácter que no sea alfanumérico
            raise CoreValidationError(
                _("Your password must contain at least one special character."),
                code='password_no_special',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one lower case, one upper case and one special character."
        )

class SpanishPhoneValidator:
    def __call__(self, phone_number):
        phone_regex = re.compile(r'^(6|7)\d{8}$')  # Los números móviles españoles comienzan con 6 o 7 y tienen 9 dígitos
        
        if not phone_regex.match(phone_number):
            raise SerializerValidationError(
                _("The given phone number is not a valid Spanish phone number. It must start with 6 or 7, and must have a length of 9 digits."),
                code='invalid_spanish_phone_number',
            )

    def get_help_text(self):
        return _("The phone number must be a valid Spanish phone number that starts with 6 or 7 and must have a length of 9 digits.")

    def deconstruct(self):
        return ('sivaria.validators.validators.SpanishPhoneValidator', [], {})

    def __eq__(self, other):
        return isinstance(other, SpanishPhoneValidator)