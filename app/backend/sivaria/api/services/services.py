from ...models import *
from ..serializers import *
from django.http import Http404, HttpResponseBadRequest
from django.contrib.auth.hashers import make_password, check_password

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
            raise Http404 
        except AppUser.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 usuario con el mismo email')
    
    def get_user_by_userId(self, userId):
        try:
            return AppUser.objects.get(userId=userId)
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


    def get_user_by_email_json(self, email):
        return AppUserSerializer(self.get_user_by_email(email)).data
        
    def get_user_by_userId_json(self, userId):
        return AppUserSerializer(self.get_user_by_userId(userId)).data
        
    def get_user_by_phone_json(self, phone):
        return AppUserSerializer(self.get_user_by_phone(phone)).data

    def hash_password(self, password):
        return make_password(password=password)
        #salt = os.urandom(32)
        #return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations= 1000)
    
    def verify_password(self, password, hash_password):
        return check_password(password=password, encoded=hash_password)
    
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
