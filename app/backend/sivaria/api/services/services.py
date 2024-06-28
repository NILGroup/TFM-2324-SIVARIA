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

import os 
import sys
'''
current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, '../../../../../scripts'))
from controller import Controller
'''

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


class UserHasParentService(object):

    def get_user_has_parent_by_son(self, id_son):
        try:
            return UserHasParent.objects.get(id_son=id_son)
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
    
class PushNotificationTypeService:

    def get_push_notification_type_by_slug(self, slug):
        try:
            return PushNotificationType.objects.get(slug=slug)
        except PushNotificationType.DoesNotExist:
            raise Http404('Registro no encontrado') 
        
    def get_push_notification_type_by_slug_json(self, slug):
        return PushNotificationTypeSerializer(self.get_push_notification_type_by_slug(slug)).data

class ExpoService:

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
'''
class ExpertSystemService():
    
    controller = None

    def __init__(self):
       self.controller = Controller() 

    def predict(self, model_type, user_data_sivaria):
        argc = ['controller.py', '-mt', str(model_type)]
        _ = self.controller.execute(argc)
        argc = ['controller.py', '-st', 'accuracy']
        _ = self.controller.execute(argc)


        csv = self.__convertToDataframe__(user_data_sivaria)
        argc = ['controller.py', '-p', '']
        result = self.controller.execute(argc)

        return result
    
    def __convertToDataframe__(self, user_data_sivaria):
        return None
'''