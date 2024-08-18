from rest_framework.serializers import Serializer, CharField, EmailField, ModelSerializer, PrimaryKeyRelatedField
from ..models import *
from django.contrib.auth import authenticate, login, logout
from rest_framework.serializers import ValidationError


class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class AppUserUpdateSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

class AppUserSerializer(ModelSerializer):
    rol = PrimaryKeyRelatedField(queryset=Rol.objects.all(), many=False)
    class Meta:
        model = AppUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone', 'code', 'rol', 'expo_token', 'birth_date')

class AppUserCompleteSerializer(ModelSerializer):
    rol = RolSerializer(many=False)
    class Meta:
        model = AppUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'code','phone', 'rol', 'expo_token', 'birth_date')


class AppUserRegisterSerializer(Serializer):
    
    class Meta:
        model = AppUser
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'rol', 'expo_token', 'birth_date')
    
    def create(self, clean_data):
        first_name = clean_data['first_name']
        last_name = clean_data['last_name']
        birth_date = clean_data['birth_date']
        birth_date_formatted = birth_date.replace('/', '')
        day, month, year = birth_date.split('/')
        birth_date_django_format = year + '-' + month + '-' + day
        code = first_name[0].upper() + last_name[0].upper() + birth_date_formatted
        user_obj = AppUser.objects.create_user(
            email=clean_data['email'],
            password=clean_data['password'],
            first_name=clean_data['first_name'],
            last_name=clean_data['last_name'],
            phone=clean_data['phone'],
            rol=clean_data['rol'],
            expo_token=clean_data['expo_token'],
            code=code,
            birth_date=birth_date_django_format
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
    child = PrimaryKeyRelatedField(queryset=AppUser.objects.all(), many=False)
    responsible = PrimaryKeyRelatedField(queryset=AppUser.objects.all(), many=False)
    class Meta:
        model = UserHasParent
        fields = ('id', 'child', 'email_parent_1', 'email_parent_2', 'responsible')

class UserHasParentModificationSerializer(Serializer):
    class Meta:
        model = UserHasParent
        fields = ('id', 'child', 'email_parent_1', 'email_parent_2', 'responsible')

    def create(self, clean_data):
        uhp_obj = UserHasParent.objects.create(
            child=clean_data['child'],
            email_parent_1=clean_data['email_parent_1'],
            email_parent_2=clean_data['email_parent_2'],
            responsible=clean_data['responsible'],
        )

        uhp_obj.save()
        return uhp_obj
    
class PushNotificationTypeSerializer(ModelSerializer):
    class Meta:
        model = PushNotificationType
        fields = '__all__'

        
class EmailTemplateSerializer(ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = '__all__'

class SenaSerializer(ModelSerializer):
    class Meta:
        model = SenaForm
        fields = '__all__'

class InqSerializer(ModelSerializer):
    class Meta:
        model = InqForm
        fields = '__all__'

class RrssSerializer(ModelSerializer):
    class Meta:
        model = RrssForm
        fields = '__all__'
    
class MulticageCad4Serializer(ModelSerializer):
    class Meta:
        model = MulticageCad4Form
        fields = '__all__'

class EbipqEcipqSerializer(ModelSerializer):
    class Meta:
        model = EbipqEcipqForm
        fields = '__all__'

class CerqsSerializer(ModelSerializer):
    class Meta:
        model = CerqsForm
        fields = '__all__'

class AtiSerializer(ModelSerializer):
    class Meta:
        model = AtiForm
        fields = '__all__'

class AteSerializer(ModelSerializer):
    class Meta:
        model = AteForm
        fields = '__all__'

class EdSerializer(ModelSerializer):
    class Meta:
        model = EdForm
        fields = '__all__'

class ErSerializer(ModelSerializer):
    class Meta:
        model = ErForm
        fields = '__all__'

class FamilySerializer(ModelSerializer):
    class Meta:
        model = FamilySubForm
        fields = '__all__'

class InjurySerializer(ModelSerializer):
    class Meta:
        model = InjuryForm
        fields = '__all__'

class ParqSerializer(ModelSerializer):
    class Meta:
        model = ParqForm
        fields = '__all__'

class SocialDataSerializer(ModelSerializer):
    class Meta:
        model = SocialDataForm
        fields = '__all__'

class SenaFamilySerializer(ModelSerializer):
    class Meta:
        model = SenaFamilyForm
        fields = '__all__'


class YoungFormSerializer(ModelSerializer):
    class Meta:
        model = YoungForm
        fields = '__all__'

class FamilyFormSerializer(ModelSerializer):
    class Meta:
        model = FamilyForm
        fields = '__all__'
    
class ProfessionalFormSerializer(ModelSerializer):
    class Meta:
        model = ProfessionalForm
        fields = '__all__'
