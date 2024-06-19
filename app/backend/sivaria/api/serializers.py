from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from ..models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')

class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class AppUserSerializer(ModelSerializer):
    id_rol = PrimaryKeyRelatedField(queryset=Rol.objects.all(), many=False)
    class Meta:
        model = AppUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone', 'id_rol')
'''
class AppUserRegisterSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fiels = '__all__'
    
    def create(self, clean_data):
        user_obj = AppUser.objects.create_user(
            email=clean_data['email'],
            password=clean_data['password'],
            first_name=clean_data['first_name'],
            last_name=clean_data['last_name'],
            phone=clean_data['phone'],
            rol=clean_data['id_rol'],
        )

        user_obj.save()
        return user_obj

class AppUserLoginSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fiels = '__all__'
    
    def create(self, clean_data):
        user_obj = AppUser.objects.create_user(
            email=clean_data['email'],
            password=clean_data['password'],
            first_name=clean_data['first_name'],
            last_name=clean_data['last_name'],
            phone=clean_data['phone'],
            rol=clean_data['id_rol'],
        )

        user_obj.save()
        return user_obj
    

class AppUserLogoutSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fiels = '__all__'
    
    def create(self, clean_data):
        user_obj = AppUser.objects.create_user(
            email=clean_data['email'],
            password=clean_data['password'],
            first_name=clean_data['first_name'],
            last_name=clean_data['last_name'],
            phone=clean_data['phone'],
            rol=clean_data['id_rol'],
        )

        user_obj.save()
        return user_obj
'''

class UserHasParentSerializer(ModelSerializer):
    id_son = PrimaryKeyRelatedField(queryset=AppUser.objects.all(), many=False)
    class Meta:
        model = UserHasParent
        fields = ('id', 'id_son', 'phone_parent_1', 'phone_parent_2')

    def create_user_has_parent(self, clean_data):
        id_user = clean_data['id_son']
        user_has_parent = UserHasParent.objects.create(id_son=id_user, )
        user_has_parent.save()
        return user_has_parent