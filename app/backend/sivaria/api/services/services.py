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
    
    def mapData(self, user_id, sivaria_data, rol_slug):
        decoded_bytes = base64.b64decode(sivaria_data)
        json_str = decoded_bytes.decode('utf-8')
        mapped_data = json.loads(json_str)
        
        #mapped_data = None
        if rol_slug == 'joven':
            mapped_data = self.__mapYoungData(sivaria_data=mapped_data)
        elif rol_slug == 'familia':
            mapped_data = self.__mapFamilyData(sivaria_data=mapped_data)
        elif rol_slug == 'profesional':
            mapped_data = self.__mapProfessionalData(sivaria_data=mapped_data)

        mapped_data['id'] = user_id
        #print(mapped_data)
        return base64.b64encode(json.dumps(mapped_data).encode('utf-8'))

    def __mapYoungData(self, sivaria_data):

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

        family1, family2, family3, family4, family5, family6, family7, family8 = self.__get_family(sivaria_data.get('step12', {}))

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
    def __mapFamilyData(self, sivaria_data):
        #id,curso,situacion_laboral_madre,situacion_laboral_padre,nivel_profesional_madre,nivel_profesional_padre,problemas_interiorizados,problemas_exteriorizados,problemas_contexto,problemas_recursos_psicologicos,madre_adolescente,padre_adolescente,padres_divorciados,familia_monoparental,tratamiento_psicologico_padre_madre,adiccion_padre_madre,relaciones_conflictivas_hijo_padre_madre,familia_reconstruida,aceptacion_rechazo_parental,control_parental,situacion_economica_precaria,ingreso_familiar_mensual,desenlace
        general_variables = self.__get_sociodemographic_variables({})

        sena1, sena2, sena3, sena4 = self.__get_sena(sivaria_data.get('step11', {}))

        family1, family2, family3, family4, family5, family6, family7, family8 = self.__get_family(sivaria_data.get('step12', {}))

        return {
            'curso': general_variables.get('curso'),
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

            'aceptacion_rechazo_parental': '',
            'control_parental': '',
            'situacion_economica_precaria': '',
            'ingreso_familiar_mensual': '',

        }
    
    def __mapProfessionalData(self, sivaria_data):
        #id,curso,situacion_laboral_madre,situacion_laboral_padre,nivel_profesional_madre,nivel_profesional_padre,situacion_economica_precaria,ingreso_familiar_mensual,tratamiento_psiquiatrico_previo,problemas_interiorizados,problemas_exteriorizados,problemas_contexto,problemas_recursos_psicologicos,madre_adolescente,padre_adolescente,padres_divorciados,familia_monoparental,tratamiento_psicologico_padre_madre,adiccion_padre_madre,relaciones_conflictivas_hijo_padre_madre,familia_reconstruida,supervision_parental_insuficiente,maltrato_al_adolescente,maltrato_a_la_pareja,duelo,desenlace
        general_variables = self.__get_sociodemographic_variables({})

        family1, family2, family3, family4, family5, family6, family7, family8 = self.__get_family(sivaria_data.get('step12', {}))

        return {
            'curso': general_variables.get('curso'),
            'situacion_laboral_madre': general_variables.get('situacion_laboral_madre'),
            'situacion_laboral_padre': general_variables.get('situacion_laboral_padre'),
            'nivel_profesional_madre': general_variables.get('nivel_profesional_madre'),
            'nivel_profesional_padre': general_variables.get('nivel_profesional_padre'),
            
            'madre_adolescente': family1,
            'padre_adolescente': family2,
            'padres_divorciados': family3,
            'familia_monoparental': family4,
            'tratamiento_psicologico_padre_madre': family5,
            'adiccion_padre_madre': family6,
            'relaciones_conflictivas_hijo_padre_madre': family7,
            'familia_reconstruida': family8,

            'supervision_parental_insuficiente': '',
            'maltrato_al_adolescente': '',
            'maltrato_a_la_pareja': '',
            'duelo': '',
            'situacion_economica_precaria': '',
            'ingreso_familiar_mensual': '',
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
    
    def __get_sena(self, data):
        
        try:
            sena_interiorizado = int(data.get('sena111', 0)) + int(data.get('sena112', 0)) + int(data.get('sena137', 0)) + int(data.get('sena141', 0))
            sena_exteriorizado = int(data.get('sena23', 0)) + int(data.get('sena103', 0)) + int(data.get('sena139', 0)) + int(data.get('sena146', 0))
            sena_contexto = int(data.get('sena19', 0)) + int(data.get('sena99', 0)) + int(data.get('sena115', 0)) + int(data.get('sena150', 0))
            sena_recursos_psicologicos = int(data.get('sena69', 0)) + int(data.get('sena117', 0)) + int(data.get('sena129', 0)) + int(data.get('sena188', 0))
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
        padres_divorciados = data.get('family4', 'no')
        familia_monoparental = data.get('family3', 'no')
        tratamiento_psicologico_padre_madre = data.get('family5', 'no')
        adiccion_padre_madre = data.get('family6', 'no')
        relaciones_conflictivas_hijo_padre_madre = data.get('family7', 'no')
        familia_reconstruida = data.get('family8', 'no')

        return (madre_adolescente,
        padre_adolescente,
        padres_divorciados,
        familia_monoparental,
        tratamiento_psicologico_padre_madre,
        adiccion_padre_madre,
        relaciones_conflictivas_hijo_padre_madre,
        familia_reconstruida)

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
        