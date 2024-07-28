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

from datetime import datetime

'''
current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, '../../../../../scripts'))
from controller import Controller
'''

from django.core.mail import send_mail

from ...expert_system.controller import Controller

import pandas as pd

import base64
import json

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

    def get_user_by_code(self, code):
        try:
            return AppUser.objects.get(code=code)
        except AppUser.DoesNotExist:
            raise Http404('Usuario no encontrado') 
        except AppUser.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 usuario con el mismo código')

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
    
    def get_user_by_code_json(self, code):
        return AppUserCompleteSerializer(self.get_user_by_code(code)).data

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

    def get_user_has_parent_by_son(self, child_id):
        try:
            return UserHasParent.objects.get(child_id=child_id)
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
        
    def get_children_by_email_parent(self, email):
        list_Children_1 = list(UserHasParent.objects.filter(email_parent_1=email))
        list_children_2 = list(UserHasParent.objects.filter(email_parent_2=email))
        return (list_Children_1 + list_children_2)
    
    def get_children_by_responsible(self, responsible_id):
        return list(UserHasParent.objects.filter(responsible=responsible_id))

    def get_user_has_parent_by_son_json(self, child_id):
        return UserHasParentSerializer(self.get_user_has_parent_by_son(child_id)).data

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
    
    def map_data(self, user, sivaria_data, rol_slug):
        form_instance = None
        
        if rol_slug == 'joven':
            form_instance = self.__save_young_data(user, sivaria_data)
            mapped_data = self.__map_young_data(sivaria_data=sivaria_data)
        elif rol_slug == 'padre' or rol_slug == 'madre':
            form_instance = self.__save_family_data(user, sivaria_data)
            mapped_data = self.__map_family_data(sivaria_data=sivaria_data)
        elif rol_slug == 'profesional':
            form_instance = self.__save_professional_data(user, sivaria_data)
            mapped_data = self.__map_professional_data(sivaria_data=sivaria_data)

        mapped_data['id'] = user.get('id', None)
        #print(mapped_data)
        return (form_instance,
                mapped_data
            )
    
    def __save_young_data(self, user, sivaria_data):
        #user_service = UserService()
        user_id = user.get('id', None)
        #user = user_service.get_user_by_userId(userId=user_id)
        
        now = datetime.now()
        versionDateTime = now.strftime("%Y%m%d%H%M%S")
        
        step1 = sivaria_data.get('step1', {})
        step2 = sivaria_data.get('step2', {})
        step3 = sivaria_data.get('step3', {})

        general_data = {}
        general_data.update(step1)
        general_data.update(step2)
        general_data.update(step3)

        social_data_form = {
            'code': 'YSOCIAL'+str(user_id)+versionDateTime,
            'course': general_data.get('course', None),
            'age': general_data.get('age', None),
            'gender': general_data.get('gender', None),
            'trans': general_data.get('trans', None),
            'job_situation_father': general_data.get('jobSituationFather', None),
            'job_situation_mother': general_data.get('jobSituationMother', None),
            'academic_level_father': general_data.get('academicLevelFather', None),
            'academic_level_mother': general_data.get('academicLevelMother', None),
            'academic_performance': general_data.get('academicPerformance', None),
            'previous_psychiatric_treatment': general_data.get('previousPsychiatricTreatment', None),
            'chronic_disease': general_data.get('chronicDisease', None),
            'female_self_perception': general_data.get('femaleSelfPerception', None),
            'male_self_perception': general_data.get('maleSelfPerception', None),
            'female_others_perception': general_data.get('femaleOthersPerception', None),
            'male_others_perception': general_data.get('maleOthersPerception', None),
            'weight': general_data.get('weight', None),
            'height': general_data.get('height', None),
            'discrimination_type': general_data.get('discriminationType', None),
        }

        step4 = sivaria_data.get('step4', {})
        ebipq_ecipq_data = {
            'code': 'YEBIPQECIPQ'+str(user_id)+versionDateTime,
            'vb1': step4.get('vb1', None), 
            'vb2': step4.get('vb2', None),
            'vb4': step4.get('vb4', None),
            'ab1': step4.get('ab1', None),
            'ab2': step4.get('ab2', None),
            'ab4': step4.get('ab4', None),
            'cybv1': step4.get('cybv1', None),
            'cybv2': step4.get('cybv2', None),
            'cybv3': step4.get('cybv3', None),
            'cybb1': step4.get('cybb1', None),
            'cybb2': step4.get('cybb2', None),
            'cybb3': step4.get('cybb3', None),
        }
        step5 = sivaria_data.get('step5', {})
        rrss_data = {
            'code': 'YRRSS'+str(user_id)+versionDateTime,
            'rrss1': step5.get('rrss1', None),
            'rrss2': step5.get('rrss2', None),
            'rrss3': step5.get('rrss3', None),
            'rrss4': step5.get('rrss4', None),
            'rrss5': step5.get('rrss5', None),
            'rrss6': step5.get('rrss6', None),
            'rrss7': step5.get('rrss7', None),
        }
        step6 = sivaria_data.get('step6', {})
        mcad_data = {
            'code': 'YMULTICAGECAD4'+str(user_id)+versionDateTime,
            'mcad1': step6.get('mcad1', None),
            'mcad2': step6.get('mcad2', None),
            'mcad3': step6.get('mcad3', None),
            'mcad4': step6.get('mcad4', None),
            'mcad5': step6.get('mcad5', None),
            'mcad6': step6.get('mcad6', None),
            'mcad7': step6.get('mcad7', None),
            'mcad8': step6.get('mcad8', None),
            'mcad9': step6.get('mcad9', None),
            'mcad10': step6.get('mcad10', None),
            'mcad11': step6.get('mcad11', None),
            'mcad12': step6.get('mcad12', None),
        }
        step7 = sivaria_data.get('step7', {})
        cerqs_data = {
            'code': 'YRRSS'+str(user_id)+versionDateTime,
            'cerqs1': step7.get('cerqs1', None), 
            'cerqs2': step7.get('cerqs2', None),
            'cerqs3': step7.get('cerqs3', None),
            'cerqs4': step7.get('cerqs4', None),
            'cerqs5': step7.get('cerqs5', None),
            'cerqs6': step7.get('cerqs6', None),
            'cerqs7': step7.get('cerqs7', None),
            'cerqs8': step7.get('cerqs8', None),
            'cerqs9': step7.get('cerqs9', None),
            'cerqs10': step7.get('cerqs10', None),
            'cerqs11': step7.get('cerqs11', None),
            'cerqs12': step7.get('cerqs12', None),
            'cerqs13': step7.get('cerqs13', None),
            'cerqs14': step7.get('cerqs14', None),
            'cerqs15': step7.get('cerqs15', None),
            'cerqs16': step7.get('cerqs16', None),
            'cerqs17': step7.get('cerqs17', None),
            'cerqs18': step7.get('cerqs18', None),
        }
        step8 = sivaria_data.get('step8', {})
        ati_data = {
            'code': 'YRRSS'+str(user_id)+versionDateTime,
            'ati1': step8.get('ati1', None),
            'ati2': step8.get('ati2', None),
            'ati3': step8.get('ati3', None),
            'ati4': step8.get('ati4', None),
            'ati5': step8.get('ati5', None),
            'ati6': step8.get('ati6', None),
        }
        ate_data = {
            'code': 'YRRSS'+str(user_id)+versionDateTime,
            'ate1': step8.get('ate1', None),
            'ate2': step8.get('ate2', None),
            'ate3': step8.get('ate3', None),
            'ate4': step8.get('ate4', None),
            'ate5': step8.get('ate5', None),
            'ate6': step8.get('ate6', None),
            'ate7': step8.get('ate7', None),
            'ate8': step8.get('ate8', None),
            'ate9': step8.get('ate9', None),
            'ate10': step8.get('ate10', None),
        }
        step9 = sivaria_data.get('step9', {})
        ed_data = {
            'code': 'YRRSS'+str(user_id)+versionDateTime,
            'ed1':step9.get('ed1', None),
            'ed2':step9.get('ed2', None),
            'ed3':step9.get('ed3', None),
            'ed4':step9.get('ed4', None),
            'ed5':step9.get('ed5', None),
            'ed6':step9.get('ed6', None),
            'ed7':step9.get('ed7', None),
            'ed8':step9.get('ed8', None),
            'ed9':step9.get('ed9', None),
            'ed10':step9.get('ed10', None),
            'ed11':step9.get('ed11', None),
            'ed12':step9.get('ed12', None),
            'ed13':step9.get('ed13', None),
            'ed14':step9.get('ed14', None),
            'ed15':step9.get('ed15', None),
            'ed16':step9.get('ed16', None),
        }
        er_data = {
            'code': 'YRRSS'+str(user_id)+versionDateTime,
            'er1':step9.get('er1', None),
            'er2':step9.get('er2', None),
            'er3':step9.get('er3', None),
            'er4':step9.get('er4', None),
            'er5':step9.get('er5', None),
            'er6':step9.get('er6', None),
            'er7':step9.get('er7', None),
            'er8':step9.get('er8', None),
            'er9':step9.get('er9', None),
            'er10':step9.get('er10', None),
        }
        inq_data = sivaria_data.get('step10', {})
        inq_data['code'] = 'YINQ'+str(user_id)+versionDateTime

        step11 = sivaria_data.get('step11', {})
        sena_data = {
            'code': 'YSENA'+str(user_id)+versionDateTime,
            'sena19': step11.get('sena19', None),
            'sena23': step11.get('sena23', None),
            'sena69': step11.get('sena69', None),
            'sena99': step11.get('sena99', None),
            'sena103': step11.get('sena103', None),
            'sena111': step11.get('sena111', None),
            'sena112': step11.get('sena112', None),
            'sena115': step11.get('sena115', None),
            'sena117': step11.get('sena117', None),
            'sena129': step11.get('sena129', None),
            'sena137': step11.get('sena137', None),
            'sena139': step11.get('sena139', None),
            'sena141': step11.get('sena141', None),
            'sena146': step11.get('sena146', None),
            'sena150': step11.get('sena150', None),
            'sena188': step11.get('sena188', None),
        }

        injury_data = {
            'code': 'YINJURY'+str(user_id)+versionDateTime,
            'injury1': step11.get('injury1', None),
        }
        step12 = sivaria_data.get('step12', {})
        family_data = {
            'code': 'YFAMILY'+str(user_id)+versionDateTime,
            'padre_adolescente': step12.get('family1', None),
            'madre_adolescente': step12.get('family2', None),
            'padres_divorciados': step12.get('family3', None),
            'familia_monoparental': step12.get('family4', None),
            'tratamiento_psicologico_padre_madre': step12.get('family5', None),
            'adiccion_padre_madre': step12.get('family6', None),
            'relaciones_conflictivas_hijo_padre_madre': step12.get('family7', None),
            'familia_reconstruida': step12.get('family8', None),
            'supervision_parental_insuficiente': step12.get('family9', None),
            'maltrato_al_adolescente': step12.get('family10', None),
            'maltrato_a_la_pareja': step12.get('family11', None),
            'ingreso_familiar_mensual': step12.get('family12', None),
            'situacion_economica_precaria': step12.get('family13', None),
            'duelo': step12.get('family14', None),
        }

        social_data_serializer = SocialDataSerializer(data=social_data_form)
        ebipq_ecipq_serializer = EbipqEcipqSerializer(data=ebipq_ecipq_data)
        rrss_serializer = RrssSerializer(data=rrss_data)
        mcad_serializer = MulticageCad4Serializer(data=mcad_data)
        cerqs_serializer = CerqsSerializer(data=cerqs_data)
        ati_serializer = AtiSerializer(data=ati_data)
        ate_serializer = AteSerializer(data=ate_data)
        ed_serializer = EdSerializer(data=ed_data)
        er_serializer = ErSerializer(data=er_data)
        inq_serializer = InqSerializer(data=inq_data)
        sena_serializer = SenaSerializer(data=sena_data)
        injury_serializer = InjurySerializer(data=injury_data)
        family_serializer = FamilySerializer(data=family_data)  
        
        if (social_data_serializer.is_valid() and
            ebipq_ecipq_serializer.is_valid() and
            rrss_serializer.is_valid() and
            mcad_serializer.is_valid() and
            cerqs_serializer.is_valid() and
            ati_serializer.is_valid() and
            ate_serializer.is_valid() and
            ed_serializer.is_valid() and
            er_serializer.is_valid() and
            inq_serializer.is_valid() and
            sena_serializer.is_valid() and
            injury_serializer.is_valid() and
            family_serializer.is_valid()
        ):
            social_data = social_data_serializer.save()
            ebipq_ecipq = ebipq_ecipq_serializer.save()
            rrss = rrss_serializer.save()
            mcad = mcad_serializer.save()
            cerqs = cerqs_serializer.save()
            ati = ati_serializer.save()
            ate = ate_serializer.save()
            ed = ed_serializer.save()
            er = er_serializer.save()
            inq = inq_serializer.save()
            sena = sena_serializer.save()
            injury = injury_serializer.save()
            family = family_serializer.save()
            
            code = 'Y'+str(user_id)+versionDateTime
            young_form_data = {
                'participant_young_form': user_id,
                'date': now,
                'code': code,
                'social_data': social_data.id,
                'ebipq_ecipq': ebipq_ecipq.id,
                'rrss': rrss.id,
                'mcad': mcad.id,
                'cerqs': cerqs.id,
                'ati': ati.id,
                'ate': ate.id,
                'ed': ed.id,
                'er': er.id,
                'inq': inq.id,
                'sena': sena.id,
                'injury': injury.id,
                'family': family.id,
            }
            
            young_serializer = YoungFormSerializer(data=young_form_data)
            if (young_serializer.is_valid()):
                young_form = young_serializer.save()
                print('Young data saved successfully.\n')
                return young_form

    def __save_family_data(self, user, sivaria_data):
        user_service = UserService()
        #print(sivaria_data)
    
        rol = user.get('rol' , None)
        rol_slug = rol.get('slug')
        family_code = 'P' if rol_slug == 'padre' else 'M'
        #print('CODIGO DEL NIÑO: ' + str(child_code))
        
        step1 = sivaria_data.get('step1', None)
        child_code = step1.get('idChild', None)
        child = user_service.get_user_by_code(code=child_code)

        user_id = user.get('id', None)

        
        now = datetime.now()
        versionDateTime = now.strftime("%Y%m%d%H%M%S")
        
        step1 = sivaria_data.get('step1', {})
        step3 = sivaria_data.get('step3', {})

        general_data = {}
        general_data.update(step1)
        general_data.update(step3)

        social_data_form = {
            'code': family_code+'SOCIAL'+str(user_id)+versionDateTime,
            'course': general_data.get('course', None),
            'job_situation_father': general_data.get('jobSituationFather', None),
            'job_situation_mother': general_data.get('jobSituationMother', None),
            'academic_level_father': general_data.get('academicLevelFather', None),
            'academic_level_mother': general_data.get('academicLevelMother', None),
        }

        step2 = sivaria_data.get('step2', {})
        sena_family_data = {
            'code': family_code+'SENAFAMILY'+str(user_id)+versionDateTime,
            'sena104': step2.get('sena104', None),
            'sena117': step2.get('sena117', None),
            'sena118': step2.get('sena118', None),
            'sena121': step2.get('sena121', None),
            'sena123': step2.get('sena123', None),
            'sena124': step2.get('sena124', None),
            'sena125': step2.get('sena125', None),
            'sena135': step2.get('sena135', None),
            'sena137': step2.get('sena137', None),
            'sena138': step2.get('sena138', None),
            'sena139': step2.get('sena139', None),
            'sena140': step2.get('sena140', None),
            'sena145': step2.get('sena145', None),
            'sena146': step2.get('sena146', None),
            'sena148': step2.get('sena148', None),
            'sena154': step2.get('sena154', None),
        }

        family_data = {
            'code': family_code+'FAMILY'+str(user_id)+versionDateTime,
            'padre_adolescente': step3.get('family1', None),
            'madre_adolescente': step3.get('family2', None),
            'padres_divorciados': step3.get('family3', None),
            'familia_monoparental': step3.get('family4', None),
            'tratamiento_psicologico_padre_madre': step3.get('family5', None),
            'adiccion_padre_madre': step3.get('family6', None),
            'relaciones_conflictivas_hijo_padre_madre': step3.get('family7', None),
            'familia_reconstruida': step3.get('family8', None),
            'ingreso_familiar_mensual': step3.get('family12', None),
            'situacion_economica_precaria': step3.get('family13', None),
        }

        step4 = sivaria_data.get('step4', {})
        step5 = sivaria_data.get('step5', {})

        parq_data_complete = {}
        parq_data_complete.update(step4)
        parq_data_complete.update(step5)

        parq_data = {
            'code': family_code+'PARQ'+str(user_id)+versionDateTime,
            'parq1' : parq_data_complete.get('parq1', None),
            'parq2' : parq_data_complete.get('parq2', None),
            'parq3' : parq_data_complete.get('parq3', None),
            'parq4' : parq_data_complete.get('parq4', None),
            'parq5' : parq_data_complete.get('parq5', None),
            'parq6' : parq_data_complete.get('parq6', None),
            'parq7' : parq_data_complete.get('parq7', None),
            'parq8' : parq_data_complete.get('parq8', None),
            'parq9' : parq_data_complete.get('parq9', None),
            'parq10': parq_data_complete.get('parq10', None),
            'parq11': parq_data_complete.get('parq11', None),
            'parq12': parq_data_complete.get('parq12', None),
            'parq13': parq_data_complete.get('parq13', None),
            'parq14': parq_data_complete.get('parq14', None),
            'parq15': parq_data_complete.get('parq15', None),
            'parq16': parq_data_complete.get('parq16', None),
            'parq17': parq_data_complete.get('parq17', None),
            'parq18': parq_data_complete.get('parq18', None),
            'parq19': parq_data_complete.get('parq19', None),
            'parq20': parq_data_complete.get('parq20', None),
            'parq21': parq_data_complete.get('parq21', None),
            'parq22': parq_data_complete.get('parq22', None),
            'parq23': parq_data_complete.get('parq23', None),
            'parq24': parq_data_complete.get('parq24', None),
            'parq25': parq_data_complete.get('parq25', None),
            'parq26': parq_data_complete.get('parq26', None),
            'parq27': parq_data_complete.get('parq27', None),
            'parq28': parq_data_complete.get('parq28', None),
            'parq29': parq_data_complete.get('parq29', None),
        }

        social_data_serializer = SocialDataSerializer(data=social_data_form)
        sena_family_serializer = SenaFamilySerializer(data=sena_family_data)
        family_serializer = FamilySerializer(data=family_data)  
        parq_serializer = ParqSerializer(data=parq_data) 
        
        if (social_data_serializer.is_valid() and
            sena_family_serializer.is_valid() and
            family_serializer.is_valid() and
            parq_serializer.is_valid()
        ):
            social_data = social_data_serializer.save()
            sena_family = sena_family_serializer.save()
            family = family_serializer.save()
            parq = parq_serializer.save()
            
            code = family_code+str(user_id)+versionDateTime
            family_form_data = {
                'participant_family_form': user_id,
                'to_user_family_form': child.id,
                'date': now,
                'code': code,
                'social_data': social_data.id,
                'family': family.id,
                'sena_family': sena_family.id,
                'parq': parq.id,
            }
            
            family_serializer = FamilyFormSerializer(data=family_form_data)
            if (family_serializer.is_valid()):
                family_form = family_serializer.save()
                print('Family form data saved successfully.\n')
                return family_form
            
    def __save_professional_data(self, user, sivaria_data):
        user_service = UserService()
        #print(sivaria_data)
        code = 'PR'
        #print('CODIGO DEL NIÑO: ' + str(child_code))
        
        step1 = sivaria_data.get('step1', None)
        print(step1)
        patient_code = step1.get('idPatient', None)
        patient = user_service.get_user_by_code(code=patient_code)

        user_id = user.get('id', None)

        now = datetime.now()
        versionDateTime = now.strftime("%Y%m%d%H%M%S")
        
        # CREANDO JSON PARA LA EL GUARDADO EN BBDD
        step1 = sivaria_data.get('step1', {})
        step2 = sivaria_data.get('step2', {})

        general_data = {}
        general_data.update(step1)
        general_data.update(step2)

        social_data_form = {
            'code': code+'SOCIAL'+str(user_id)+versionDateTime,
            'course': general_data.get('course'),
            'job_situation_father': general_data.get('jobSituationFather', None),
            'job_situation_mother': general_data.get('jobSituationMother', None),
            'academic_level_father': general_data.get('academicLevelFather', None),
            'academic_level_mother': general_data.get('academicLevelMother', None),
        }

        family_data_complete = {}
        step2 = sivaria_data.get('step2', {})
        step3 = sivaria_data.get('step3', {})
        
        family_data_complete.update(step2)
        family_data_complete.update(step3)
        
        family_data = {
            'code': code+'FAMILY'+str(user_id)+versionDateTime,
            'padre_adolescente': family_data_complete.get('family1', None),
            'madre_adolescente': family_data_complete.get('family2', None),
            'padres_divorciados': family_data_complete.get('family3', None),
            'familia_monoparental': family_data_complete.get('family4', None),
            'tratamiento_psicologico_padre_madre': family_data_complete.get('family5', None),
            'adiccion_padre_madre': family_data_complete.get('family6', None),
            'relaciones_conflictivas_hijo_padre_madre': step3.get('family7', None),
            'familia_reconstruida': family_data_complete.get('family8', None),
            'supervision_parental_insuficiente': family_data_complete.get('family9', None),
            'maltrato_al_adolescente': family_data_complete.get('family10', None),
            'maltrato_a_la_pareja': family_data_complete.get('family11', None),
            'ingreso_familiar_mensual': family_data_complete.get('family12', None),
            'situacion_economica_precaria': family_data_complete.get('family13', None),
            'duelo': family_data_complete.get('family14', None),
        }

        social_data_serializer = SocialDataSerializer(data=social_data_form)
        family_serializer = FamilySerializer(data=family_data)  
        
        if (social_data_serializer.is_valid() and
            family_serializer.is_valid()
        ):
            social_data = social_data_serializer.save()
            family = family_serializer.save()
            
            code = code+str(user_id)+versionDateTime
            professional_form_data = {
                'participant_professional_form': user_id,
                'to_user_professional_form': patient.id,
                'date': now,
                'code': code,
                'social_data': social_data.id,
                'family': family.id,
            }
            
            professional_serializer = ProfessionalFormSerializer(data=professional_form_data)
            if (professional_serializer.is_valid()):
                professional_form = professional_serializer.save()
                print('Professional form data saved successfully.\n')
                return professional_form


    def __map_young_data(self, sivaria_data):

        #try:
        step1 = sivaria_data.get('step1', {})
        step2 = sivaria_data.get('step2', {})
        step3 = sivaria_data.get('step3', {})
        general_data = {}
        general_data.update(step1)
        general_data.update(step2)
        general_data.update(step3)
        general_variables = self.__get_sociodemographic_variables(general_data)

        bullying_victima, bullying_perpetrador, cyberbullying_victima, cyberbullying_perpetrador = self.__get_ebipq_ecipq(sivaria_data.get('step4', {}))

        rrss1, rrss2, rrss3, rrss4, rrss5, rrss6, rrss7 = self.__get_rrss(sivaria_data.get('step5', {}))

        adiccion_alcohol, adiccion_sustancias, adiccion_internet = self.__get_multicage_cad4(sivaria_data.get('step6', {}))

        nivel_regulacion_positiva, nivel_regulacion_negativa = self.__get_cerqs(sivaria_data.get('step7', {}))

        atrapamiento_interno = self.__get_ati(sivaria_data.get('step8', {}))
        atrapamiento_externo = self.__get_ate(sivaria_data.get('step8', {}))

        nivel_percibido_derrota = self.__get_ed(sivaria_data.get('step9', {}))
        nivel_resiliencia = self.__get_er(sivaria_data.get('step9', {}))
        
        percepcion_ser_una_carga, sentido_pertenencia_frustada = self.__get_inq(sivaria_data.get('step10', {}))
    
        sena1, sena2, sena3, sena4 = self.__get_sena(sivaria_data.get('step11', {}))
        
        injury = self.__get_fasm(sivaria_data.get('step11', {}))

        family1, family2, family3, family4, family5, family6, family7, family8, _, _, _, _, _, _ = self.__get_family(sivaria_data.get('step12', {}))

        #except Exception as e:
            #raise Exception(str(e))
                
        return {
            'edad': general_variables.get('edad'),
            'curso': general_variables.get('curso'),
            'peso': general_variables.get('peso'),
            'altura': general_variables.get('altura'),
            'sexo_asignado': general_variables.get('sexo_asignado'),
            'transgenero': general_variables.get('transgenero'),
            'nivel_promedio_academico': general_variables.get('nivel_promedio_academico'),
            'situacion_laboral_madre': general_variables.get('situacion_laboral_madre'),
            'situacion_laboral_padre': general_variables.get('situacion_laboral_padre'),
            'nivel_profesional_madre': general_variables.get('nivel_profesional_madre'),
            'nivel_profesional_padre': general_variables.get('nivel_profesional_padre'),
            'nivel_autopercepcion_masculina': general_variables.get('nivel_autopercepcion_masculina'),
            'nivel_autopercepcion_femenina': general_variables.get('nivel_autopercepcion_femenina'),
            'nivel_percepcion_masculina_externa': general_variables.get('nivel_percepcion_masculina_externa'),
            'nivel_percepcion_femenina_externa': general_variables.get('nivel_percepcion_femenina_externa'),
            'tratamiento_psiquiatrico_previo': general_variables.get('tratamiento_psiquiatrico_previo'),
            'enfermedad_cronica': general_variables.get('enfermedad_cronica'),

            'bullying_victima': bullying_victima,
            'bullying_perpetrador': bullying_perpetrador,
            'cyberbullying_victima': cyberbullying_victima,
            'cyberbullying_perpetrador': cyberbullying_perpetrador,
            
            'adiccion_alcohol': adiccion_alcohol,
            'adiccion_sustancias': adiccion_sustancias,
            'adiccion_internet': adiccion_internet,
            
            'problemas_interiorizados': sena1,
            'problemas_exteriorizados': sena2,
            'problemas_contexto': sena3,
            'problemas_recursos_psicologicos': sena4,
            
            'fuente_discriminacion': general_variables.get('fuente_discriminacion'),
            
            'nivel_resiliencia': nivel_resiliencia,
            'nivel_regulacion_positiva': nivel_regulacion_positiva,
            'nivel_regulacion_negativa': nivel_regulacion_negativa,
            
            'atrapamiento_interno': atrapamiento_interno,
            'atrapamiento_externo': atrapamiento_externo,
            'nivel_percibido_fracaso': nivel_percibido_derrota,
            'sentido_pertenencia_frustrada': sentido_pertenencia_frustada,
            'percepcion_de_ser_una_carga': percepcion_ser_una_carga,
            'autoeficiencia_para_el_suicidio': injury,
            
            'madre_adolescente': family1,
            'padre_adolescente': family2,
            'padres_divorciados': family3,
            'familia_monoparental': family4,
            'tratamiento_psicologico_padre_madre': family5,
            'adiccion_padre_madre': family6,
            'relaciones_conflictivas_hijo_padre_madre': family7,
            'familia_reconstruida': family8,
            
            'busqueda_informacion_autolesion': rrss1,
            'compartir_en_rrss_pensamiento_autolesion': rrss2,
            'peticion_de_ayuda_en_internet': rrss3,
            'realizacion_autolesion_despues_de_ver_contenido': rrss4,
            'tener_conocidos_que_comparten_autolesion_internet': rrss5,
            'contacto_informacion_autolesion': rrss6,
            'denuncia_autolesion_internet': rrss7,
        }
    def __map_family_data(self, sivaria_data):
        #id,curso,situacion_laboral_madre,situacion_laboral_padre,nivel_profesional_madre,nivel_profesional_padre,problemas_interiorizados,problemas_exteriorizados,problemas_contexto,problemas_recursos_psicologicos,madre_adolescente,padre_adolescente,padres_divorciados,familia_monoparental,tratamiento_psicologico_padre_madre,adiccion_padre_madre,relaciones_conflictivas_hijo_padre_madre,familia_reconstruida,aceptacion_rechazo_parental,control_parental,situacion_economica_precaria,ingreso_familiar_mensual,desenlace
        
        step1 = sivaria_data.get('step1', {})
        step3 = sivaria_data.get('step3', {})

        general_data = {}
        general_data.update(step1)
        general_data.update(step3)
        general_variables = self.__get_sociodemographic_variables(general_data)

        general_variables = self.__get_sociodemographic_variables(general_data)

        sena1, sena2, sena3, sena4 = self.__get_sena(sivaria_data.get('step2', {}), family=1)

        family1, family2, family3, family4, family5, family6, family7, family8, _, _, _, family12, family13, _ = self.__get_family(sivaria_data.get('step3', {}))

        step4 = sivaria_data.get('step4', {})
        step5 = sivaria_data.get('step5', {})

        parq_data = {}
        parq_data.update(step4)
        parq_data.update(step5)
        aceptacion_rechazo_parental, control_parental = self.__get_parq(parq_data)

        return {
            'curso': general_variables.get('curso'),
            'situacion_laboral_madre': general_variables.get('situacion_laboral_madre'),
            'situacion_laboral_padre': general_variables.get('situacion_laboral_padre'),
            'nivel_profesional_madre': general_variables.get('nivel_profesional_madre'),
            'nivel_profesional_padre': general_variables.get('nivel_profesional_padre'),

            'problemas_interiorizados': sena1,
            'problemas_exteriorizados': sena2,
            'problemas_contexto': sena3,
            'problemas_recursos_psicologicos': sena4,

            'madre_adolescente': family1,
            'padre_adolescente': family2,
            'padres_divorciados': family3,
            'familia_monoparental': family4,
            'tratamiento_psicologico_padre_madre': family5,
            'adiccion_padre_madre': family6,
            'relaciones_conflictivas_hijo_padre_madre': family7,
            'familia_reconstruida': family8,

            'aceptacion_rechazo_parental': aceptacion_rechazo_parental,
            'control_parental': control_parental,
            'situacion_economica_precaria': family13,
            'ingreso_familiar_mensual': family12,

        }
    
    def __map_professional_data(self, sivaria_data):
        #id,curso,situacion_laboral_madre,situacion_laboral_padre,nivel_profesional_madre,nivel_profesional_padre,situacion_economica_precaria,ingreso_familiar_mensual,tratamiento_psiquiatrico_previo,problemas_interiorizados,problemas_exteriorizados,problemas_contexto,problemas_recursos_psicologicos,madre_adolescente,padre_adolescente,padres_divorciados,familia_monoparental,tratamiento_psicologico_padre_madre,adiccion_padre_madre,relaciones_conflictivas_hijo_padre_madre,familia_reconstruida,supervision_parental_insuficiente,maltrato_al_adolescente,maltrato_a_la_pareja,duelo,desenlace

        step1 = sivaria_data.get('step1', None)
        step2 = sivaria_data.get('step2', None)
        step3 = sivaria_data.get('step3', None)

        general_data = {}
        general_data.update(step1)
        general_data.update(step2)
        general_variables = self.__get_sociodemographic_variables(general_data)
        
        family_data = {}
        step2 = sivaria_data.get('step2', None)
        step3 = sivaria_data.get('step3', None)
        family_data.update(step2)
        family_data.update(step3)

        family1, family2, family3, family4, family5, family6, family7, family8, family9 , family10, family11, family12, family13, family14 = self.__get_family(family_data)

        return {
            'curso': general_variables.get('curso'),
            'situacion_laboral_madre': general_variables.get('situacion_laboral_madre'),
            'situacion_laboral_padre': general_variables.get('situacion_laboral_padre'),
            'nivel_profesional_madre': general_variables.get('nivel_profesional_madre'),
            'nivel_profesional_padre': general_variables.get('nivel_profesional_padre'),
            'situacion_economica_precaria': family13,
            'ingreso_familiar_mensual': family12,
            'tratamiento_psiquiatrico_previo': general_variables.get('tratamiento_psiquiatrico_previo'),
            
            'madre_adolescente': family1,
            'padre_adolescente': family2,
            'padres_divorciados': family3,
            'familia_monoparental': family4,
            'tratamiento_psicologico_padre_madre': family5,
            'adiccion_padre_madre': family6,
            'relaciones_conflictivas_hijo_padre_madre': family7,
            'familia_reconstruida': family8,

            'supervision_parental_insuficiente': family9,
            'maltrato_al_adolescente': family10,
            'maltrato_a_la_pareja': family11,
            'duelo': family14,
        }

    def __get_sociodemographic_variables(self, data):
        course = data.get('course', '').replace('_', ' ')
        age = self.__decodeAge(int(data.get('age', 0)))
        gender = data.get('gender', '')
        trans = data.get('trans', '').replace('_', ' ')
    
        job_situation_father = data.get('jobSituationFather', '').replace('_', ' ')
        job_situation_mother = data.get('jobSituationMother', '').replace('_', ' ')
        academic_level_father = data.get('academicLevelFather', '').replace('_', ' ')
        academic_level_mother = data.get('academicLevelMother', '').replace('_', ' ')
        academic_performance = data.get('academicPerformance', '').replace('_', ' ')
        previous_psychiatric_treatment = data.get('previousPsychiatricTreatment', '')
        chronic_disease = data.get('chronicDisease', '')
        
        female_self_perception = int(data.get('femaleSelfPerception', 0))
        male_self_perception = int(data.get('maleSelfPerception', 0))
        female_others_perception = int(data.get('femaleOthersPerception', 0))
        male_others_perception = int(data.get('maleOthersPerception', 0))
        weight = self.__decodeWeight(float(data.get('weight', 0)))
        height = self.__decodeHeight(float(data.get('height', 0)))
        discrimination_type = data.get('discriminationType', '')

        return {
            'edad': age,
            'curso': course,
            'peso': weight,
            'altura': height,
            'sexo_asignado': gender,
            'transgenero': trans,
            'nivel_promedio_academico': academic_performance,
            'situacion_laboral_madre': job_situation_mother,
            'situacion_laboral_padre': job_situation_father,
            'nivel_profesional_madre': academic_level_mother,
            'nivel_profesional_padre': academic_level_father,
            'nivel_autopercepcion_masculina': male_self_perception,
            'nivel_autopercepcion_femenina': female_self_perception,
            'nivel_percepcion_masculina_externa': male_others_perception,
            'nivel_percepcion_femenina_externa': female_others_perception,
            'tratamiento_psiquiatrico_previo': previous_psychiatric_treatment,
            'enfermedad_cronica': chronic_disease,
            'fuente_discriminacion': discrimination_type,
        }

    def __get_ebipq_ecipq(self, data):
        # da error si alguno de las variables es = ''
        try:
            vb = int(data.get('vb1', 0)) + int(data.get('vb2', 0)) + int(data.get('vb4', 0))
            ab = int(data.get('ab1', 0)) + int(data.get('ab2', 0)) + int(data.get('ab4', 0))
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario EBIP-Q')
        try:
            cybv = int(data.get('cybv3', 0)) + int(data.get('cybv3', 0)) + int(data.get('cybv3', 0))
            cybb = int(data.get('cybb3', 0)) + int(data.get('cybb3', 0)) + int(data.get('cybb3', 0))
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario ECIP-Q')

        bullying_victima = 'si' if vb > 6 else 'no'
        bullying_perpetrador = 'si' if ab > 6 else 'no'
        cyberbullying_victima = 'si' if cybv > 6 else 'no'
        cyberbullying_perpetrador = 'si' if cybb > 6 else 'no'

        return (bullying_victima, bullying_perpetrador, cyberbullying_victima, cyberbullying_perpetrador)

    def __get_multicage_cad4(self, data):
        # da error si alguno de las variables es = ''
        countAlcoholAddiction = 0
        countSubstanceAddiction = 0
        countInternetAddiction = 0
        
        for mcad_index in range(1, 4):
            mcad = data.get('mcad'+str(mcad_index), 'no')
            countAlcoholAddiction += 1 if mcad.lower() == 'si' else 0
        
        for mcad_index in range(5, 8):
            mcad = data.get('mcad'+str(mcad_index), 'no')
            countSubstanceAddiction += 1 if mcad.lower() == 'si' else 0
            
        for mcad_index in range(9, 12):
            mcad = data.get('mcad'+str(mcad_index), 'no')
            countInternetAddiction += 1 if mcad.lower() == 'si' else 0

        adiccion_alcohol = 'si' if countAlcoholAddiction >= 2 else 'no'
        adiccion_sustancias = 'si' if countSubstanceAddiction >= 2 else 'no'
        adiccion_internet = 'si' if countInternetAddiction >= 2 else 'no'

        return (adiccion_alcohol, adiccion_sustancias, adiccion_internet)
    
    def __get_sena(self, data, family = 0):
        
        try:
            sena_interiorizado =  ((
                int(data.get('sena111', 0)) + 
                int(data.get('sena112', 0)) + 
                int(data.get('sena137', 0)) + 
                int(data.get('sena141', 0))
            ) if family == 0 else 
            (
                int(data.get('sena135', 0)) + 
                int(data.get('sena138', 0)) + 
                int(data.get('sena140', 0)) + 
                int(data.get('sena145', 0))
            ))

            sena_exteriorizado = ((
                int(data.get('sena23', 0)) + 
                int(data.get('sena103', 0)) + 
                int(data.get('sena139', 0)) + 
                int(data.get('sena146', 0))
            ) if family == 0 else 
            (
                int(data.get('sena117', 0)) + 
                int(data.get('sena121', 0)) + 
                int(data.get('sena123', 0)) + 
                int(data.get('sena124', 0))        
            ))

            sena_contexto = ((
                int(data.get('sena19', 0)) + 
                int(data.get('sena99', 0)) + 
                int(data.get('sena115', 0)) + 
                int(data.get('sena150', 0))
            ) if family == 0 else 
            (
                int(data.get('sena104', 0)) + 
                int(data.get('sena118', 0)) + 
                int(data.get('sena125', 0)) + 
                int(data.get('sena148', 0))
            ))

            sena_recursos_psicologicos = ((
                int(data.get('sena69', 0)) + 
                int(data.get('sena117', 0)) + 
                int(data.get('sena129', 0)) + 
                int(data.get('sena188', 0))
            ) if family == 0 else 
            (
                int(data.get('sena137', 0)) + 
                int(data.get('sena139', 0)) + 
                int(data.get('sena146', 0)) + 
                int(data.get('sena154', 0))
            ))
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario SENA')
    
        problemas_interiorizados = 'si' if sena_interiorizado > 10 else 'no'
        problemas_exteriorizados = 'si' if sena_exteriorizado > 10 else 'no'
        problemas_contexto = 'si' if sena_contexto > 10 else 'no'
        problemas_recursos_psicologicos = 'si' if sena_recursos_psicologicos > 10 else 'no'

        return (problemas_interiorizados,
                problemas_exteriorizados,
                problemas_contexto,
                problemas_recursos_psicologicos)

    def __get_ati(self, data): # OK
        try:
            ati = (int(data.get('ati1', 0)) + 
                   int(data.get('ati2', 0)) + 
                   int(data.get('ati3', 0)) + 
                   int(data.get('ati4', 0)) + 
                   int(data.get('ati5', 0)) + 
                   int(data.get('ati6', 0)))
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario ATI')

        atrapamiento_interno = 'si' if ati > 12 else 'no'

        return (atrapamiento_interno)

    def __get_ate(self, data): # OK
        try:
            ate = (int(data.get('ate1', 0)) + 
                   int(data.get('ate2', 0)) + 
                   int(data.get('ate3', 0)) + 
                   int(data.get('ate4', 0)) + 
                   int(data.get('ate5', 0)) + 
                   int(data.get('ate6', 0)) + 
                   int(data.get('ate7', 0)) + 
                   int(data.get('ate8', 0)) + 
                   int(data.get('ate9', 0)) + 
                   int(data.get('ate10', 0)))
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario ATE')

        atrapamiento_externo = 'si' if ate > 10 else 'no'

        return (atrapamiento_externo)

    def __get_ed(self, data): # OK
        try:
            ed2_reversed = self.__reverse_scale(4, int(data.get('ed2', 4)))
            ed4_reversed = self.__reverse_scale(4, int(data.get('ed4', 4)))
            ed9_reversed = self.__reverse_scale(4, int(data.get('ed9', 4)))
            ed = (int(data.get('ed1', 0)) + 
                   ed2_reversed + 
                   int(data.get('ed3', 0)) + 
                   ed4_reversed + 
                   int(data.get('ed5', 0)) + 
                   int(data.get('ed6', 0)) + 
                   int(data.get('ed7', 0)) + 
                   int(data.get('ed8', 0)) + 
                   ed9_reversed + 
                   int(data.get('ed10', 0)) + 
                   int(data.get('ed11', 0)) + 
                   int(data.get('ed12', 0)) + 
                   int(data.get('ed13', 0)) + 
                   int(data.get('ed14', 0)) + 
                   int(data.get('ed15', 0)) + 
                   int(data.get('ed16', 0)))
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario ED')

        nivel_derrota = ''

        if ed < 21:
            nivel_derrota = 'alto'
        elif ed >= 21 and ed < 42:
            nivel_derrota = 'medio'
        elif ed >= 42 and ed <= 64:
            nivel_derrota = 'bajo'

        return (nivel_derrota)

    def __get_inq(self, data): # OK
        # de acuerdo al cuestionario INQ de SIVARIA, de la pregunta 1 a la 6 son preguntas relacionadas por la percepcion de ser una carga, 
        # las otras 9 es del sentimiento de pertenencia frustada
        try:
            inq7_reversed = self.__reverse_scale(8, int(data.get('inq7', 7)))
            inq8_reversed = self.__reverse_scale(8, int(data.get('inq8', 7)))
            inq10_reversed = self.__reverse_scale(8, int(data.get('inq10', 7)))
            inq13_reversed = self.__reverse_scale(8, int(data.get('inq13', 7)))
            inq14_reversed = self.__reverse_scale(8, int(data.get('inq14', 7)))
            inq15_reversed = self.__reverse_scale(8, int(data.get('inq15', 7)))

            inq_percepcion_carga = (int(data.get('inq1', 0)) + 
                   int(data.get('inq2', 1)) + 
                   int(data.get('inq3', 1)) + 
                   int(data.get('inq4', 1)) + 
                   int(data.get('inq5', 1)) + 
                   int(data.get('inq6', 1))) 
            inq_pertenencia_frustada = (
                   inq7_reversed + 
                   inq8_reversed + 
                   int(data.get('inq9', 1)) + 
                   inq10_reversed + 
                   int(data.get('inq11', 1)) + 
                   int(data.get('inq12', 1)) + 
                   inq13_reversed + 
                   inq14_reversed + 
                   inq15_reversed)
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario INQ')

        sentido_pertenencia_frustada = 'si' if inq_pertenencia_frustada > 21 else 'no'
        percepcion_ser_una_carga = 'si' if inq_percepcion_carga > 31 else 'no'

        return (sentido_pertenencia_frustada, percepcion_ser_una_carga)

    def __get_er(self, data): # OK
        try:
            er = (int(data.get('er1', 0)) + 
                   int(data.get('er2', 0)) + 
                   int(data.get('er3', 0)) + 
                   int(data.get('er4', 0)) + 
                   int(data.get('er5', 0)) + 
                   int(data.get('er6', 0)) + 
                   int(data.get('er7', 0)) + 
                   int(data.get('er8', 0)) + 
                   int(data.get('er9', 0)) + 
                   int(data.get('er10', 0)))
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario ER')

        nivel_resiliencia = 0
        if 0 <= er <= 8:
            nivel_resiliencia = 1
        elif 9 <= er <= 16:
            nivel_resiliencia = 2
        elif 17 <= er <= 24:
            nivel_resiliencia = 3
        elif 25 <= er <= 32:
            nivel_resiliencia = 4
        elif 33 <= er <= 40:
            nivel_resiliencia = 5
        
        return (nivel_resiliencia)

    def __get_cerqs(self, data):
        try:
            cerqs_positiva = (int(data.get('cerqs6', 0)) + 
                   int(data.get('cerqs8', 0)) + 
                   int(data.get('cerqs9', 0)) + 
                   int(data.get('cerqs12', 0)) + 
                   int(data.get('cerqs13', 0)) + 
                   int(data.get('cerqs14', 0)) + 
                   int(data.get('cerqs15', 0)))
            cerqs_negativa = (int(data.get('cerqs1', 0)) + 
                   int(data.get('cerqs2', 0)) + 
                   int(data.get('cerqs3', 0)) + 
                   int(data.get('cerqs4', 0)) + 
                   int(data.get('cerqs5', 0)) + 
                   int(data.get('cerqs7', 0)) + 
                   int(data.get('cerqs10', 0)) + 
                   int(data.get('cerqs11', 0)) + 
                   int(data.get('cerqs16', 0)) + 
                   int(data.get('cerqs17', 0))+ 
                   int(data.get('cerqs18', 0)))
        except ValueError as e:
            raise ValueError('Hay un valor o valores vacíos dentro del cuestionario CERQ-S')

        nivel_regulacion_positiva = 0
        if 7 <= cerqs_positiva <= 12:
            nivel_regulacion_positiva = 1
        elif 13 <= cerqs_positiva <= 17:
            nivel_regulacion_positiva = 2
        elif 18 <= cerqs_positiva <= 22:
            nivel_regulacion_positiva = 3
        elif 23 <= cerqs_positiva <= 27:
            nivel_regulacion_positiva = 4
        elif 28 <= cerqs_positiva <= 35:
            nivel_regulacion_positiva = 5

        nivel_regulacion_negativa = 0
        if 11 <= cerqs_negativa <= 17:
            nivel_regulacion_negativa = 1
        elif 18 <= cerqs_negativa <= 26:
            nivel_regulacion_negativa = 2
        elif 27 <= cerqs_negativa <= 35:
            nivel_regulacion_negativa = 3
        elif 36 <= cerqs_negativa <= 44:
            nivel_regulacion_negativa = 4
        elif 45 <= cerqs_negativa <= 55:
            nivel_regulacion_negativa = 5
        
        return(nivel_regulacion_positiva,
               nivel_regulacion_negativa)

    def __get_fasm(self, data):
        if not data.get('injury1'):
            raise ValueError('Valor vacío en el cuestionario de la autolesion')
        return data.get('injury1', 'no')

    def __get_family(self, data):

        padre_adolescente = 'si' if int(data.get('family1', 21)) < 21 else 'no'
        madre_adolescente = 'si' if int(data.get('family2', 21)) < 21 else 'no'
        familia_monoparental = data.get('family3', 'no')
        padres_divorciados = data.get('family4', 'no')
        tratamiento_psicologico_padre_madre = data.get('family5', 'no')
        adiccion_padre_madre = data.get('family6', 'no')
        relaciones_conflictivas_hijo_padre_madre = data.get('family7', 'no')
        familia_reconstruida = data.get('family8', 'no')
        supervision_parental_insuficiente = data.get('family9', 'no')
        maltrato_al_adolescente = data.get('family10', 'no')
        maltrato_a_la_pareja = data.get('family11', 'no')
        ingreso_familiar_mensual = self.__decodeMonthlyFamiliarIncome(float(data.get('family12', 0)))
        situacion_economica_precaria = data.get('family13', 'no')
        duelo = data.get('family14', 'no')

        return (madre_adolescente,
            padre_adolescente,
            padres_divorciados,
            familia_monoparental,
            tratamiento_psicologico_padre_madre,
            adiccion_padre_madre,
            relaciones_conflictivas_hijo_padre_madre,
            familia_reconstruida,
            supervision_parental_insuficiente,
            maltrato_al_adolescente,
            maltrato_a_la_pareja,
            ingreso_familiar_mensual,
            situacion_economica_precaria,
            duelo
        )

    def __get_rrss(self, data):
        # da error si alguno de las variables es = ''
        contacto_informacion_autolesion = data.get('rrss1', 'no')
        busqueda_informacion_autolesion =  data.get('rrss2', 'no')
        compartir_en_rrss_pensamiento_autolesion = data.get('rrss3', 'no')
        peticion_de_ayuda_en_internet = data.get('rrss4', 'no')
        realizacion_autolesion_despues_de_ver_contenido = data.get('rrss5', 'no')
        denuncia_autolesion_internet = data.get('rrss6', 'no')
        tener_conocidos_que_comparten_autolesion_internet = data.get('rrss7', 'no')

        return (busqueda_informacion_autolesion, 
                compartir_en_rrss_pensamiento_autolesion, 
                peticion_de_ayuda_en_internet,
                realizacion_autolesion_despues_de_ver_contenido,
                tener_conocidos_que_comparten_autolesion_internet,
                contacto_informacion_autolesion,
                denuncia_autolesion_internet)

    def __get_parq(self, data):
        print(data)
        parq1_reversed = self.__reverse_scale(5, int(data.get('parq1', 0)))
        parq3_reversed = self.__reverse_scale(5, int(data.get('parq3', 0)))
        parq7_reversed = self.__reverse_scale(5, int(data.get('parq7', 0)))
        parq10_reversed = self.__reverse_scale(5, int(data.get('parq10', 0)))
        parq13_reversed = self.__reverse_scale(5, int(data.get('parq13', 0)))
        parq18_reversed = self.__reverse_scale(5, int(data.get('parq18', 0)))
        parq23_reversed = self.__reverse_scale(5, int(data.get('parq23', 0)))
        parq29_reversed = self.__reverse_scale(5, int(data.get('parq29', 0)))
        
        afecto = (
            parq1_reversed +
            parq3_reversed +
            parq7_reversed +
            parq10_reversed +
            parq13_reversed +
            parq18_reversed +
            parq23_reversed +
            parq29_reversed
        )
        
        hostilidad = (
            int(data.get('parq4', 0)) + 
            int(data.get('parq8', 0)) + 
            int(data.get('parq12', 0)) + 
            int(data.get('parq14', 0)) + 
            int(data.get('parq20', 0)) + 
            int(data.get('parq24', 0))
        )

        indiferencia = (
            int(data.get('parq9', 0)) + 
            int(data.get('parq15', 0)) + 
            int(data.get('parq17', 0)) + 
            int(data.get('parq22', 0)) + 
            int(data.get('parq25', 0)) + 
            int(data.get('parq28', 0))
        )
        rechazo_indiferenciado = (
            int(data.get('parq3', 0)) + 
            int(data.get('parq16', 0)) + 
            int(data.get('parq19', 0)) + 
            int(data.get('parq21', 0))
        )

        aceptacion_rechazo_parental_score = (
            afecto + 
            hostilidad + 
            indiferencia + 
            rechazo_indiferenciado
        )

        control = (
            int(data.get('parq2', 0)) + 
            int(data.get('parq5', 0)) + 
            int(data.get('parq6', 0)) + 
            int(data.get('parq11', 0)) + 
            int(data.get('parq27', 0))
        )
        aceptacion_rechazo_parental = 'Aceptacion' if aceptacion_rechazo_parental_score > 60 else 'Rechazo'
        control_parental = 'si' if control > 10 else 'no'
        return (aceptacion_rechazo_parental,
                control_parental)

    def __reverse_scale(self, limit, value):
        if limit < value:
            raise Exception('El inverso de la puntuación sale negativo')
        return limit - value

    def __decodeAge(self, age):
        if age >= 12 and age <= 16:
            return '12-16'
        elif age == 17 or age == 18:
            return '17-18'
        elif age >=19 and age <= 21:
            return '19-21'
        else:
            return False
        
    def __decodeWeight(self, weight):
        if weight <= 49:
            return "x<=49".upper()
        elif weight >= 50 or weight < 70:
            return "50-69"
        elif weight >= 70 or weight < 90:
            return "80-89"
        elif weight >= 90:
            return "x>=90".upper()
        else:
            return False
    
    def __decodeHeight(self, height):
        if height <= 149:
            return "x<=149".upper()
        elif height >= 150 or height < 170:
            return "150-169"
        elif height >= 170 or height < 190:
            return "180-189"
        elif height >= 190:
            return "x>=190".upper()
        else:
            return False
        
    def __decodeMonthlyFamiliarIncome(self, income):
        if income <= 999:
            return "X<=999"
        elif income >= 1000 and income < 1500:
            return "1000-1499"
        elif income >= 1500 and income < 1999:
            return "1500-1999"
        elif income >= 2000:
            return "X>=2000"
        else:
            return False

    
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

class FormService(object):
    
    def __init__(self): 
        pass

    def get_form_by_code(self, initial_code, code):
        try:
            model = None
            if initial_code == 'Y':
                model = YoungForm
            elif initial_code == 'P' or initial_code == 'M':
                model = FamilyForm
            elif initial_code == 'PR':
                model = ProfessionalForm
                
            return model.objects.get(code=code)
        except model.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except model.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_form_by_code_json(self, initial_code, code):
        data = None
        if initial_code == 'Y':
            data = YoungFormSerializer(self.get_form_by_code(initial_code, code)).data
        elif initial_code == 'P' or initial_code == 'M':
            data = FamilyFormSerializer(self.get_form_by_code(initial_code, code)).data
        elif initial_code == 'PR':
            data = ProfessionalFormSerializer(self.get_form_by_code(initial_code, code)).data

        return data

    def get_sena_form_by_id(self, sena_id):
        try:
            return SenaForm.objects.get(id=sena_id)
        except SenaForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except SenaForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_sena_form_by_id_json(self, sena_id):
        return SenaSerializer(self.get_sena_form_by_id(sena_id)).data
    
    
    def get_family_subform_by_id(self, family_id):
        try:
            return FamilySubForm.objects.get(id=family_id)
        except FamilySubForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except FamilySubForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_family_subform_by_id_json(self, family_id):
        return FamilySerializer(self.get_family_subform_by_id(family_id)).data
    
    
    def get_social_data_by_id(self, social_data_id):
        try:
            return SocialDataForm.objects.get(id=social_data_id)
        except SocialDataForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except SenaForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_social_data_by_id_json(self, social_data_id):
        return SocialDataSerializer(self.get_social_data_by_id(social_data_id)).data
    
    
    def get_sena_family_by_id(self, sena_family_id):
        try:
            return SenaFamilyForm.objects.get(id=sena_family_id)
        except SenaFamilyForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except SenaFamilyForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_sena_family_by_id_json(self, sena_family_id):
        return SenaFamilySerializer(self.get_sena_family_by_id(sena_family_id)).data
    
    
    def get_parq_by_id(self, parq_id):
        try:
            return ParqForm.objects.get(id=parq_id)
        except ParqForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except ParqForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_parq_by_id_json(self, parq_id):
        return ParqSerializer(self.get_parq_by_id(parq_id)).data
    
    def get_er_by_id(self, er_id):
        try:
            return ErForm.objects.get(id=er_id)
        except ErForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except ErForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_er_by_id_json(self, er_id):
        return ErSerializer(self.get_er_by_id(er_id)).data
    
    def get_ed_by_id(self, ed_id):
        try:
            return EdForm.objects.get(id=ed_id)
        except EdForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except EdForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_ed_by_id_json(self, ed_id):
        return EdSerializer(self.get_ed_by_id(ed_id)).data
    
    def ebipq_ecipq_id(self, ebipq_ecipq_id):
        try:
            return EbipqEcipqForm.objects.get(id=ebipq_ecipq_id)
        except EbipqEcipqForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except EbipqEcipqForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_ebipq_ecipq_by_id_json(self, ebipq_ecipq_id):
        return EbipqEcipqSerializer(self.ebipq_ecipq_id(ebipq_ecipq_id)).data
    
    def get_rrss_by_id(self, rrss_id):
        try:
            return RrssForm.objects.get(id=rrss_id)
        except RrssForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except RrssForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_rrss_by_id_json(self, rrss_id):
        return RrssSerializer(self.get_rrss_by_id(rrss_id)).data
    
    def get_mcad_by_id(self, mcad_id):
        try:
            return MulticageCad4Form.objects.get(id=mcad_id)
        except MulticageCad4Form.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except MulticageCad4Form.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_mcad_by_id_json(self, mcad_id):
        return MulticageCad4Serializer(self.get_mcad_by_id(mcad_id)).data
    
    def get_cerqs_by_id(self, cerqs_id):
        try:
            return CerqsForm.objects.get(id=cerqs_id)
        except CerqsForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except CerqsForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_cerqs_by_id_json(self, cerqs_id):
        return CerqsSerializer(self.get_cerqs_by_id(cerqs_id)).data
    
    def get_ati_by_id(self, ati_id):
        try:
            return AtiForm.objects.get(id=ati_id)
        except AtiForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except AtiForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_ati_by_id_json(self, ati_id):
        return AtiSerializer(self.get_ati_by_id(ati_id)).data
    
    def get_inq_by_id(self, inq_id):
        try:
            return InqForm.objects.get(id=inq_id)
        except InqForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except InqForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_inq_by_id_json(self, inq_id):
        return InqSerializer(self.get_inq_by_id(inq_id)).data
    
    def get_sena_by_id(self, sena_id):
        try:
            return SenaForm.objects.get(id=sena_id)
        except SenaForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except SenaForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_sena_by_id_json(self, sena_id):
        return SenaSerializer(self.get_sena_by_id(sena_id)).data
    
    def get_injury_by_id(self, injury_id):
        try:
            return InjuryForm.objects.get(id=injury_id)
        except InjuryForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except InjuryForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_injury_by_id_json(self, injury_id):
        return InjurySerializer(self.get_injury_by_id(injury_id)).data
    
    
    
    def get_ate_by_id(self, ate_id):
        try:
            return AteForm.objects.get(id=ate_id)
        except AteForm.DoesNotExist:
            raise Http404('Formulario no encontrado')
        except AteForm.MultipleObjectsReturned:
            raise HttpResponseBadRequest('Se ha encontrado más de 1 formulario con el mismo código')
        
    def get_ate_by_id_json(self, ate_id):
        return AteSerializer(self.get_ate_by_id(ate_id)).data

        
    def get_form_info(self, user, code):
        user_service = UserService()

        initial_code = code[0:2] if code[0:2] == 'PR' else code[0]
        #print(initial_code)
        user_id = user.get('id')

        form = self.get_form_by_code(initial_code, code)
        form_data = {}
        if initial_code == 'Y':
            user = user_service.get_user_by_userId(form.participant_young_form.id)

            social_data = self.get_social_data_by_id_json(form.social_data.id)
            ebipq_ecipq = self.get_ebipq_ecipq_by_id_json(form.ebipq_ecipq.id)
            rrss = self.get_rrss_by_id_json(form.rrss.id)
            mcad = self.get_mcad_by_id_json(form.mcad.id)
            cerqs = self.get_cerqs_by_id_json(form.cerqs.id)
            ati = self.get_ati_by_id_json(form.ati.id)
            ate = self.get_ate_by_id_json(form.ate.id)
            ed = self.get_ed_by_id_json(form.ed.id)
            er = self.get_er_by_id_json(form.er.id)
            inq = self.get_inq_by_id_json(form.inq.id)
            sena = self.get_sena_by_id_json(form.sena.id)
            injury = self.get_injury_by_id_json(form.injury.id)
            family = self.get_family_subform_by_id_json(form.family.id)

            form_data = {
                'form_code': initial_code,
                'id': form.id,
                'user': user.first_name + ' ' + user.last_name,
                'social_data': social_data,
                'ebipq_ecipq': ebipq_ecipq,
                'rrss': rrss,
                'mcad':  mcad,
                'cerqs': cerqs,
                'ati': ati,
                'ate': ate,
                'ed': ed,
                'er': er,
                'inq': inq,
                'sena': sena,
                'injury': injury,
                'family': family,
                'datetime_str': form.date.strftime('%d/%m/%Y %H:%M:%S'),
                'result': form.prediction
            }
        elif initial_code == 'P' or initial_code == 'M':
            user = user_service.get_user_by_userId(form.participant_family_form.id)
            to_user = user_service.get_user_by_userId(form.to_user_family_form.id)
            
            social_data = self.get_social_data_by_id_json(form.social_data.id)
            family = self.get_family_subform_by_id_json(form.family.id)
            sena_family = self.get_sena_family_by_id_json(form.sena_family.id)
            parq = self.get_parq_by_id_json(form.parq.id)
        
            form_data= {
                'form_code': initial_code,
                'id': form.id,
                'user': user.first_name + ' ' + user.last_name,
                'to_user': to_user.first_name + ' ' + to_user.last_name,
                'social_data': social_data,
                'family': family,
                'sena_family': sena_family,
                'parq': parq,
                'datetime_str': form.date.strftime('%d/%m/%Y %H:%M:%S'),
                'result': form.prediction
            }
        elif initial_code == 'PR':   
            user = user_service.get_user_by_userId(form.participant_professional_form.id)
            to_user = user_service.get_user_by_userId(form.to_user_professional_form.id)

            family = self.get_family_subform_by_id_json(form.family.id)
            social_data = self.get_social_data_by_id_json(form.social_data.id)

            form_data = {
                'form_code': initial_code,
                'id': form.id,
                'code': form.code,
                'user': user.first_name + ' ' + user.last_name,
                'to_user': to_user.first_name + ' ' + to_user.last_name,
                'social_data': social_data,
                'family': family,
                'datetime_str': form.date.strftime('%d/%m/%Y %H:%M:%S'),
                'result': form.prediction
            }
        
        return form_data

    def get_forms_by_user_DT(self, user):
        user_service = UserService()
        total_forms = []
        rol = user.get('rol', None)
        if rol:
            rol_slug = rol.get('slug', None)
            child_forms = []
            family_forms = []
            professional_forms = []
            if rol_slug == 'padre' or rol_slug == 'madre':
                email_parent = user.get('email')
                user_has_parents_registers = (UserHasParent.objects.filter(email_parent_1=email_parent) 
                                              | UserHasParent.objects.filter(email_parent_2=email_parent))
                
                for user_has_parent_register in user_has_parents_registers:
                    child = user_has_parent_register.child
                    email_parent_1 = user_has_parent_register.email_parent_1
                    email_parent_2 = user_has_parent_register.email_parent_2
                    parent_1_id = None
                    parent_2_id = None
                    if email_parent_1:
                        parent_1 = user_service.get_user_by_email_json(email=email_parent_1)
                        parent_1_id = parent_1.get('id')
                    
                    if email_parent_2:
                        parent_2 = user_service.get_user_by_email_json(email=email_parent_2)
                        parent_2_id = parent_2.get('id')
                    
                    responsible = user_has_parent_register.responsible
                    professional_id = responsible.id

                    child_id = child.id

                    child_forms = self.__get_child_forms(child_id)
                    family_forms = self.__get_family_forms(parent_1_id, parent_2_id, child_id)                    
                    professional_forms = self.__get_professional_forms(professional_id, child_id)
                    
                    forms = child_forms + family_forms + professional_forms
                    total_forms += forms

            elif rol_slug == 'profesional':
                professional_id = user.get('id')
                #print(professional_id)

                user_has_parents_registers = UserHasParent.objects.filter(responsible=professional_id)
                #print(user_has_parents_registers)
                for user_has_parent_register in user_has_parents_registers:
                    child = user_has_parent_register.child
                    email_parent_1 = user_has_parent_register.email_parent_1
                    email_parent_2 = user_has_parent_register.email_parent_2
                    parent_1_id = None
                    parent_2_id = None
                    if email_parent_1:
                        parent_1 = user_service.get_user_by_email_json(email=email_parent_1)
                        parent_1_id = parent_1.get('id')
                    
                    if email_parent_2:
                        parent_2 = user_service.get_user_by_email_json(email=email_parent_2)
                        parent_2_id = parent_2.get('id')

                    child_id = child.id

                    child_forms = self.__get_child_forms(child_id)
                    family_forms = self.__get_family_forms(parent_1_id, parent_2_id, child_id)                    
                    professional_forms = self.__get_professional_forms(professional_id, child_id)

                    forms = child_forms + family_forms + professional_forms
                    total_forms += forms

            if total_forms:
                total_forms = sorted(total_forms, key=lambda x: x['datetime'], reverse=True)
            #print(total_forms)
            
            #print(child_forms)
            #print(family_forms)
            #print(professional_forms)
        return total_forms
    
    def __get_child_forms(self, child_id):
        child_forms = list(YoungForm.objects.filter(participant_young_form=child_id))
        child_form_data = []
        for child_form in child_forms:
            complete_name = child_form.participant_young_form.first_name + ' ' + child_form.participant_young_form.last_name 
            child_data = {
                'code': child_form.code,
                'user': complete_name,
                'to_user': complete_name,
                'rol': 'joven',
                'datetime': child_form.date,
                'datetime_str': child_form.date.strftime('%d/%m/%Y %H:%M:%S'),
                'result': child_form.prediction,
            }
            child_form_data.append(child_data)
        
        return child_form_data
    
    def __get_family_forms(self, parent_1_id, parent_2_id, child_id):
        parent_1_forms = []
        parent_2_forms = []
        if parent_1_id:
            parent_1_forms = list(FamilyForm.objects.filter(participant_family_form=parent_1_id,
                                                            to_user_family_form=child_id))

        if parent_2_id:
            parent_2_forms = list(FamilyForm.objects.filter(participant_family_form=parent_2_id,
                                                            to_user_family_form=child_id))

        family_forms = parent_1_forms + parent_2_forms
        family_form_data = []
        for family_form in family_forms:
            complete_name_user = family_form.participant_family_form.first_name + ' ' + family_form.participant_family_form.last_name 
            complete_name_to_user = family_form.to_user_family_form.first_name + ' ' + family_form.to_user_family_form.last_name
            
            rol = family_form.participant_family_form.rol
            if rol:
                rol_slug = rol.slug

            family_data = {
                'code': family_form.code,
                'user': complete_name_user,
                'to_user': complete_name_to_user,
                'rol': rol_slug,
                'datetime': family_form.date,
                'datetime_str': family_form.date.strftime('%d/%m/%Y %H:%M:%S'),
                'result': family_form.prediction,
            }
            family_form_data.append(family_data)

        return family_form_data

    def __get_professional_forms(self, professional_id, child_id):
        professional_forms = list(ProfessionalForm.objects.filter(participant_professional_form=professional_id,
                                                                  to_user_professional_form=child_id))
        professional_form_data = []
        for professional_form in professional_forms:
            complete_name_user = professional_form.participant_professional_form.first_name + ' ' + professional_form.participant_professional_form.last_name 
            complete_name_to_user = professional_form.to_user_professional_form.first_name + ' ' + professional_form.to_user_professional_form.last_name
            
            rol = professional_form.participant_professional_form.rol
            if rol:
                rol_slug = rol.slug

            professional_data = {
                'code': professional_form.code,
                'user': complete_name_user,
                'to_user': complete_name_to_user,
                'rol': rol_slug,
                'datetime': professional_form.date,
                'datetime_str': professional_form.date.strftime('%d/%m/%Y %H:%M:%S'),
                'result': professional_form.prediction,
            }
            professional_form_data.append(professional_data)

        return professional_form_data