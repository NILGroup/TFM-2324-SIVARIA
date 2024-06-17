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


class UserHasParentSerializer(ModelSerializer):
    id_son = PrimaryKeyRelatedField(queryset=AppUser.objects.all(), many=False)
    class Meta:
        model = UserHasParent
        fields = ('id', 'id_son', 'phone_parent_1', 'phone_parent_2')
