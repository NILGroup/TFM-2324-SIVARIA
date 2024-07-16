from ...models import *
from ..serializers import *
from django.http import Http404, HttpResponseBadRequest
from django.contrib.auth.hashers import make_password, check_password

from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError

from ...validators.service_validators import UserValidator

import os 
import sys
import re
'''
current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, '../../../../../scripts'))
from controller import Controller
'''

from django.core.mail import send_mail

from ...expert_system.controller import Controller

import pandas as pd

class RolService(object):
    def get_rol_by_id(self, rolId):
        try:
            return Rol.objects.get(id=rolId)
        except Rol.DoesNotExist:
            raise Http404('Rol no encontrado')  
        except Rol.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 rol con el mismo ID')
        
    def get_rol_by_slug(self, slug):
        try:
            return Rol.objects.get(slug=slug)
        except Rol.DoesNotExist:
            raise Http404('Rol no encontrado') 
        except Rol.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 rol con el mismo slug')
    
    def get_rol_by_slug_json(self, slug):
        return RolSerializer(self.get_rol_by_slug(slug)).data

    def get_rol_by_id_json(self, rolId):
        return RolSerializer(self.get_rol_by_id(rolId)).data

    def get_all_rols_json(self):
        rol = Rol.objects.all()
        serializer = RolSerializer(rol, many=True)
        return serializer.data

    def save_rol(self, data):
        serializer = RolSerializer(data=data) 

        if serializer.is_valid():
            serializer.save()
            return (serializer.data, True)
        
        return (serializer.errors, False)
    
    def update_rol(self, rol, data, partial):
        serializer = RolSerializer(rol, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return (serializer.data, True)
        
        return (serializer.errors, False)


class UserService(object):

    validator = None
    
    def __init__(self):
        self.validator = UserValidator()

    def get_user_by_email(self, email):
        try:
            return AppUser.objects.get(email=email)
        except AppUser.DoesNotExist:
            raise Http404('Usuario no encontrado')
        except AppUser.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 usuario con el mismo email')
    
    def get_user_by_userId(self, userId):
        try:
            return AppUser.objects.get(id=userId)
        except AppUser.DoesNotExist:
            raise Http404('Usuario no encontrado') 
        except AppUser.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 usuario con el mismo ID')

    def get_user_by_phone(self, phone):
        try:
            return AppUser.objects.get(phone=phone)
        except AppUser.DoesNotExist:
            raise Http404('Usuario no encontrado') 
        except AppUser.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 usuario con el mismo teléfono')

    def get_users_by_expo_token(self, token):
        try:
            return list(AppUser.objects.filter(expo_token=token))
        except AppUser.DoesNotExist:
            raise Http404('Usuario no encontrado') 


    def get_user_by_email_json(self, email):
        return AppUserCompleteSerializer(self.get_user_by_email(email)).data
        
    def get_user_by_userId_json(self, userId):
        return AppUserCompleteSerializer(self.get_user_by_userId(userId)).data
        
    def get_user_by_phone_json(self, phone):
        return AppUserCompleteSerializer(self.get_user_by_phone(phone)).data

    def hash_password(self, password):
        return make_password(password=password)
        #salt = os.urandom(32)
        #return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations= 1000)
    
    def verify_password(self, password, hash_password):
        return check_password(password=password, encoded=hash_password)
    
    def register_user(self, data):
        serializer = AppUserRegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(data)
        return user
    
    def check_user(self, data):
        serializer = AppUserLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.check_user(data)
        return user

    def save_user(self, data):
        serializer = AppUserSerializer(data=data)  
        if serializer.is_valid():
            serializer.save()
            return (serializer.data, True)
        
        return (serializer.errors, False)
    
    def update_user(self, user, data, partial):
        serializer = AppUserSerializer(user, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return (serializer.data, True)
        
        return (serializer.errors, False)
    
    def delete_user(self, email):
        AppUser.objects.filter(email=email).delete()

    def validate_email(self, email):
        return self.validator.validate_email(email)
    
    def validate_password(self, password):
        return self.validator.validate_password(password)

    def clean_email(self, email = ''):
        try:
            local_part, domain = self.divide_email_address(email)
        except ValueError as e:
            raise AttributeError('Formato incorrecto del email')

        pattern = re.compile(r'[^a-zA-Z0-9.]')

        local_part_clean = re.sub(pattern, '', local_part)
        domain_clean = re.sub(pattern, '', domain)
        
        return f"{local_part_clean}@{domain_clean}"
    
    def divide_email_address(self, email = ''):
        email_parts = []
        if email or email != '':
            email_parts = email.strip().split('@')

        return email_parts
    
    def get_all_users_by_rol(self, rol, field = None):
        users = []
        if not field:
            users = AppUser.objects.filter(rol=rol, is_active=True).values()
        else:
            users = AppUser.objects.filter(rol=rol, is_active=True).values(field)

        return users

class UserHasParentService(object):

    def get_user_has_parent_by_son(self, son_id):
        try:
            return UserHasParent.objects.get(son_id=son_id)
        except UserHasParent.DoesNotExist:
            raise Http404('Registro no encontrado') 
        except UserHasParent.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 registro con el mismo ID de usuario')
    
    def get_user_has_parent_by_id(self, uhpId):
        try:
            return UserHasParent.objects.get(id=uhpId)
        except UserHasParent.DoesNotExist:
            raise Http404('Registro no encontrado')
        except UserHasParent.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 usuario con el ID')

    def get_user_has_parent_by_son_json(self, son_id):
        return UserHasParentSerializer(self.get_user_has_parent_by_son(son_id)).data


    def insert_user_has_parent(self, data):
        uhpSerializer = UserHasParentModificationSerializer(data=data)
        
        uhpSerializer.is_valid(raise_exception=True)
        return uhpSerializer.create(clean_data=data)

    def save_user_has_parent(self, data):
        serializer = UserHasParentSerializer(data=data)  
        if serializer.is_valid():
            serializer.save()
            return (serializer.data, True)
        
        return (serializer.errors, False)
    
    def update_user_has_parent(self, uhp, data, partial):
        serializer = UserHasParentSerializer(uhp, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return (serializer.data, True)
        
        return (serializer.errors, False)
    
class PushNotificationTypeService(object):

    def get_push_notification_type_by_slug(self, slug):
        try:
            return PushNotificationType.objects.get(slug=slug)
        except PushNotificationType.DoesNotExist:
            raise Http404('Registro no encontrado') 
        
    def get_push_notification_type_by_slug_json(self, slug):
        return PushNotificationTypeSerializer(self.get_push_notification_type_by_slug(slug)).data

class ExpoService(object):

    client = None

    def __init__(self):
        self.client = PushClient(force_fcm_v1=True)

    def send_push_messages(self, expo_tokens, title, message, data=None, sound=None):
        try:
            push_messages = []
            for token in expo_tokens:
                push_message = PushMessage(
                    to=token,
                    title= title,
                    body=message,
                    data=data,
                    sound=sound,
                    priority='high'
                )
                push_messages.append(push_message)
                
            responses = PushClient().publish_multiple(push_messages=push_messages) 
        
        except (ConnectionError, HTTPError, PushServerError) as exc:
            # Encountered some Connection or HTTP error
            raise Exception(str(exc))
        
        for response in responses:
            invalid_tokens = []
            try:
                # We got a response back, but we don't know whether it's an error yet.
                # This call raises errors so we can handle them with normal exception
                # flows.
                response.validate_response()
            except DeviceNotRegisteredError as exc:
                # Mark the push token as inactive
                #from notifications.models import PushToken
                #PushToken.objects.filter(token=token).update(active=False)
                raise Exception(str(exc))
                
            except PushTicketError as exc:
                # Encountered some other per-notification error.
                raise Exception(str(exc))
            
        return invalid_tokens

class ExpertSystemService(object):
    
    controller = None

    def __init__(self):
       self.controller = Controller() 

    def predict(self, model_type, user_data_sivaria):
        argc = ['controller.py', '-mt', str(model_type)]
        ans = self.controller.execute(argc)
        print(ans)
        #argc = ['controller.py', '-st', 'accuracy']
        #_ = self.controller.execute(argc)


        #csv = self.__convertToDataframe__(user_data_sivaria)
        argc = ['controller.py', '-p', '--json', user_data_sivaria]
        # devuelve un dataframe
        result = self.controller.execute(argc)
        #Se convierte a JSON y se devuelve
        print(result)
        return result[0]
    
class EmailTemplateService(object):
    def __init__(self): 
        pass
        
    def get_email_template_by_code(self, code):
        try:
            return EmailTemplate.objects.get(code=code)
        except EmailTemplate.DoesNotExist:
            raise Http404('Registro no encontrado') 
        except EmailTemplate.MultipleObjectsReturned:
            raise Http404('Se han encontrado más de un email template con el mismo código') 
        
    def get_email_template_by_code_json(self, code):
        return EmailTemplateSerializer(self.get_email_template_by_code(code)).data

class EmailService(object):

    def __init__(self): 
        pass

    def send_email(self, subject = '', message = '', to_mail = []):
        # to_mail must be an array
        send_mail(subject, message, None, to_mail)
        pass
        