from rest_framework.serializers import Serializer, CharField, EmailField, ModelSerializer, PrimaryKeyRelatedField
from ..models import *
from django.contrib.auth import authenticate, login, logout
from rest_framework.serializers import ValidationError


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')

class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class AppUserSerializer(ModelSerializer):
    rol = PrimaryKeyRelatedField(queryset=Rol.objects.all(), many=False)
    class Meta:
        model = AppUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone', 'rol', 'expo_token')

class AppUserCompleteSerializer(ModelSerializer):
    rol = RolSerializer(many=False)
    class Meta:
        model = AppUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone', 'rol', 'expo_token')


class AppUserRegisterSerializer(Serializer):
    
    class Meta:
        model = AppUser
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'rol', 'expo_token')
    
    def create(self, clean_data):
        user_obj = AppUser.objects.create_user(
            email=clean_data['email'],
            password=clean_data['password'],
            first_name=clean_data['first_name'],
            last_name=clean_data['last_name'],
            phone=clean_data['phone'],
            rol=clean_data['rol'],
            expo_token=clean_data['expo_token'],
        )

        user_obj.save()
        return user_obj

class AppUserLoginSerializer(Serializer):
    email = EmailField()
    password = CharField()

    class Meta:
        fields = '__all__'
    
    # Function lo login the user
    def check_user(self, clean_data):
        user = authenticate(username=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('Usuario no encontrado')
        
        return user
    

class AppUserLogoutSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fiels = 'email'


class UserHasParentSerializer(ModelSerializer):
    id_son = PrimaryKeyRelatedField(queryset=AppUser.objects.all(), many=False)
    class Meta:
        model = UserHasParent
        fields = ('id', 'id_son', 'email_parent_1', 'email_parent_2')

class UserHasParentModificationSerializer(Serializer):
    class Meta:
        model = UserHasParent
        fields = ('id', 'son', 'email_parent_1', 'email_parent_2')

    def create(self, clean_data):
        uhp_obj = UserHasParent.objects.create(
            son=clean_data['son'],
            email_parent_1=clean_data['email_parent_1'],
            email_parent_2=clean_data['email_parent_2'],
        )

        uhp_obj.save()
        return uhp_obj
    

class PushNotificationTypeSerializer(ModelSerializer):
    class Meta:
        model = PushNotificationType
        fields = '__all__'