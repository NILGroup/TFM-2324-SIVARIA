from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from .serializers import *
from django.http import Http404, HttpResponseBadRequest
from .services.services import *
import sys
# User authentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, permissions
from django.contrib.sessions.models import Session

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.serializers import ValidationError as SerializerValidationError
from django.core.exceptions import ValidationError as CoreValidationError

from rest_framework.authentication import SessionAuthentication

from django.middleware.csrf import get_token

from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator

import json
import base64

from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

'''
Type of requests to all the posts

http://127.0.0.1:8000/sivaria/v1/post

This endpoint can be a GET and POST at the same time

'''
class Post_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        
        return Response(serializer.data)    
    
    def post(self, request, format=None):

        data = {
            'title': request.data.get('title'),
            'body': request.data.get('body')
        }

        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #raise Http404
'''
Type of requests to a single Post

http://127.0.0.1:8000/sivaria/v1/post/{post_id}

This endpoint can be a GET, DELETE and PUT at the same time

'''  
class Post_APIView_Detail(APIView):    
    
    def get_object(self, postId):
        try:
            return Post.objects.get(pk=postId)
        except Post.DoesNotExist:
            raise Http404  
    
    def get(self, request, postId, format=None):
        post = self.get_object(postId)
        serializer = PostSerializer(post)  
        return Response(serializer.data)    
    
    def put(self, request, postId, format=None):
        #print('\nPOST_ID: ' + str(post_id) + '\n')
        post = self.get_object(postId)
        #print(post)
        serializer = PostSerializer(post, data=request.data, partial = True)
        #print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        #raise Http404
    
    def delete(self, request, postId, format=None):
        post = self.get_object(postId)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''

http://127.0.0.1:8000/sivaria/v1/rol

'''
class Rol_APIView(APIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = RolSerializer

    def get(self, request, format=None, *args, **kwargs):
        rolService = RolService()
        rols = rolService.get_all_rols_json()
        response = {
            'status': 'ok',
            'message': 'Datos devueltos correctamente',
            'data': {
                'rols': rols,
                'count': len(rols)
            }
        }
        return Response(response, status=status.HTTP_200_OK)  

    def post(self, request, format=None):
        rolService = RolService()

        rolData = {
            'slug': request.data.get('slug'),
            'description': request.data.get('description'),
            'code': request.data.get('code')
        }

        serializer_response, saved = rolService.save_rol(data=rolData)
        if saved:
            return Response(serializer_response, status=status.HTTP_201_CREATED)
        
        return Response(serializer_response, status=status.HTTP_400_BAD_REQUEST) 


'''
http://127.0.0.1:8000/sivaria/v1/rol/{slug}

'''
class Rol_APIView_Detail_Slug(APIView):

    def get(self, request, slug, format=None):
        rolService = RolService()
        rol_data = rolService.get_rol_by_slug_json(slug)
        response = {
            'status': 'ok',
            'message': 'Datos devueltos correctamente',
            'data': rol_data
        }
        return Response(response, status=status.HTTP_200_OK) 
    
    def put(self, request, slug, format=None):
        rolService = RolService()

        try:
            rol = rolService.get_rol_by_slug_json(slug)
        except Http404:
            response = {
                'status': 'error',
                'message': 'Rol no encontrado',
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND) 
        
        response = {
            'status': 'error',
            'message': 'Error editando el rol',
        }

        serializer_response, saved = rolService.update_rol(rol=rol, data=request.data,partial=True)

        if saved:
            response['status'] = 'ok'
            response['message'] = 'Rol actualizado correctamente'
            response['data'] = serializer_response
            return Response(response, status=status.HTTP_200_OK)
        
        response['data'] = serializer_response
        return Response(response, status=status.HTTP_400_BAD_REQUEST)   

'''
http://127.0.0.1:8000/sivaria/v1/rol/{rolId}

'''
class Rol_APIView_Detail_RolId(APIView):

    def get(self, request, rolId, format=None):
        rolService = RolService()
        rol_data = rolService.get_rol_by_id_json(rolId)
        response = {
            'status': 'ok',
            'message': 'Datos devueltos correctamente',
            'data': rol_data
        }
        return Response(response, status=status.HTTP_200_OK) 
    
    def put(self, request, rolId, format=None):
        rolService = RolService()
        
        response = {
            'status': 'error',
            'message': 'Error editando el rol',
        }
        
        try:
            rol = rolService.get_rol_by_id_json(rolId)
        except (Http404, HttpResponseBadRequest) as e:
            response['data'] = e
            return Response(response, status=status.HTTP_404_NOT_FOUND) 

        serializer_response, saved = rolService.save_rol(rol=rol, data=request.data,partial=True)

        if saved:
            response['status'] = 'ok'
            response['message'] = 'Rol actualizado correctamente'
            response['data'] = serializer_response
            return Response(response, status=status.HTTP_200_OK)
        
        response['data'] = serializer_response
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

'''
http://127.0.0.1:8000/sivaria/v1/user/register

'''
#@method_decorator(csrf_protect, name='dispatch')
class AppUser_APIView_Register(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        rol_service = RolService()
        user_has_parent_service = UserHasParentService()
        user_service = UserService()
        
        response = {
            'status': 'error',
            'message': 'Error en el registro del usuario'
        }

        if not request.data:
            response['message'] = 'Petición vacía'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        email = request.data.get('email', None)
        try:
            email_clean = user_service.clean_email(email)
        except AttributeError as e:
            response['message'] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    

        #cambiarlo por el serializador
        #rol_slug = request.data.get('rol_slug', None)
        #rol_instance = Rol.objects.get(slug=rol_slug)
        rol_slug = request.data.get('rol_slug', None)
        rol_instance = rol_service.get_rol_by_slug(rol_slug)

        data = {
            'first_name': request.data.get('first_name', None),
            'last_name': request.data.get('last_name', None),
            'email': email_clean,
            'password': request.data.get('password', None),
            'phone': request.data.get('phone', None),
            'rol': rol_instance,
            'expo_token': request.data.get('expo_token', None),
            'birth_date': request.data.get('birth_date', None),
        }

        try:
            check_user_data = user_service.get_user_by_email(email=data['email'])
            if check_user_data:
                response['message'] = 'Ya existe un usuario con este email.'
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        
        # Validate data, in this case, the serializar makes the validation job with is_valid function()
        # Email would be already validated by EmailField in model
        # Password will be validated by the validators set in AUTH_PASSWORD_VALIDATORS property in the settings.py file
        # Phone will be validated with a custom validator
        # The password will be checked in the model and hashed in the create_user function, called in the create function in the serializer

        # The user is saved in AppUser table
        #serializer_response, saved = userService.save_user(data)

        if rol_slug == 'joven':
            #user = userService.get_user_by_email_json(data['email'])
            email_parent_1 = request.data.get('email_parent_1', None)
            email_parent_2 = request.data.get('email_parent_2', None)
            email_responsible = request.data.get('email_responsible', None)
            if not email_parent_1 and not email_parent_2:
                response = {
                    'status': 'error',
                    'message': 'No se ha dado ningún email de ningún padre.'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            
            if not email_responsible:
                response = {
                    'status': 'error',
                    'message': 'No se ha asignado ningún profesional a este usuario'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            
            responsible = user_service.get_user_by_email(email=email_responsible)
            responsible_json = user_service.get_user_by_email_json(email=email_responsible)
            responsible_rol = responsible_json.get('rol', None)
            if responsible_rol:
                rol_slug = responsible_rol.get('slug', None)
                if rol_slug and rol_slug != 'profesional':
                    response = {
                        'status': 'error',
                        'message': 'El usuario asignado no tiene el rol de profesional'
                    }
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

            user = user_service.register_user(data=data)
            if user:
                uhpData = {
                    'child': user,
                    'email_parent_1': email_parent_1,
                    'email_parent_2': email_parent_2,
                    'responsible': responsible,
                }

                _ = user_has_parent_service.insert_user_has_parent(data=uhpData)

        elif rol_slug == 'padre' or rol_slug == 'madre':
            
            email_child = request.data.get('email_child', None)
            try:
                child = user_service.get_user_by_email_json(email_child)
            except Http404 as e:
                error_message = str(e)
                
                response = {
                    'status': 'error',
                    'message': error_message + '. ' + 'No hay un usuario registrado con el email ' + email_child
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            
            child_rol = child.get('rol')
            if child_rol:
                slug = child_rol.get('slug', None)
                if slug and slug !='joven':
                    response = {
                        'status': 'error',
                        'message': 'El usuario no está registrado como joven.'
                    }
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
                    
                child_id = child.get('id')
                #print(child)
                try:
                    user_has_parent = user_has_parent_service.get_user_has_parent_by_son(child_id)
                    user_has_parent_data = {}
                    email_parent_1 = user_has_parent.email_parent_1
                    email_parent_2 = user_has_parent.email_parent_2
                    if not email_parent_1:
                        user_has_parent_data['email_parent_1'] = email_clean
                    if not email_parent_2 and not user_has_parent_data.get('email_parent_1', None):
                        user_has_parent_data['email_parent_2'] = email_clean
                    else:
                        response = {
                            'status': 'error',
                            'message': 'El hijo o hija ya tiene dos padres registrados dentro de la plataforma.'
                        }
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)

                    #print(data)
                    user = user_service.register_user(data=data)
                    if user:
                        #print(user_has_parent_data)
                        #print(user_has_parent)
                        serializer_message, success = user_has_parent_service.update_user_has_parent(user_has_parent, data=user_has_parent_data, partial=True)
                        if not success:
                            response = {
                                'status': 'error',
                                'message': 'Error durante la actualización de los datos de la relación del padre con el hijo.\n' + serializer_message 
                            }
                            return Response(response, status=status.HTTP_400_BAD_REQUEST)
                    
                except Http404:
                    user = user_service.register_user(data=data)
                    if user:
                        uhpData = {
                            'child': child,
                            'email_parent_1': email_clean,
                        }
                        _ = user_has_parent_service.insert_user_has_parent(data=uhpData)
        else:
            user = user_service.register_user(data=data)

        token, created = Token.objects.get_or_create(user=user)
        response = {
            'status': 'ok',
            'message': 'Usuario registrado correctamente',
            'token': token.key
        }

        return Response(response, status=status.HTTP_201_CREATED)        
      
'''
http://127.0.0.1:8000/sivaria/v1/user/login

'''
class AppUser_APIView_Login(APIView):

    permission_classes = (permissions.AllowAny, )
    #authentication_classes = (SessionAuthentication, )

    def post(self, request, format=None):
        response = {
            'status': 'error', 
            'message': 'Error en el proceso de login del usuario.',  
        }
        user_service = UserService()
        user_has_parent_service = UserHasParentService()
        
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        try:
            user_service.validate_email(email)
        except:
            response['data'] = 'Email vacío'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:  
            user_service.validate_password(password)
        except:
            response['data'] = 'Contraseña vacía'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            email_clean = user_service.clean_email(email)
        except AttributeError as e:
            response['data'] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


        data = {
            'email': email_clean,
            'password': password
        }

        try:
            user = user_service.check_user(data)
            #login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            expo_token = request.data.get('expo_token',None)
            if expo_token is not None or expo_token == '':
                user_service.update_user(user=user, data={'expo_token': expo_token}, partial=True)
            
            user_data = user_service.get_user_by_email_json(email=data['email'])
            rol = user_data.get('rol', None)
            if rol:
                slug = rol.get('slug', None)
                if slug and slug=='joven':
                    user_has_parent_data = user_has_parent_service.get_user_has_parent_by_son_json(child_id=user_data['id'])
                    user_data['email_parent_1'] = user_has_parent_data.get('email_parent_1', None)
                    user_data['email_parent_2'] = user_has_parent_data.get('email_parent_2', None)
                    user_data['responsible'] = user_has_parent_data.get('responsible', None)
            user_data.pop('password')
            user_data.pop('expo_token')
        except:
            response['data'] = 'Usuario no encontrado'
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 
        
        response['status'] = 'ok',
        response['message'] = 'Usuario logeado correctamente',
        response['data'] = user_data
        response['token'] = token.key
        return Response(response, status=status.HTTP_200_OK)
        
        '''
        user = authenticate(username=data['email'], password=data['password'])
        if user:
            #Primer metodo de validacion
            token, _ = Token.objects.get_or_create(user=user)

            response['status']='ok'
            response['message']='Usuario logeado correctamente'
            response['data'] = {
                'token': token.key
            }
            
            return Response(response, status=status.HTTP_200_OK)
            #Segundo metodo de validacion
            login(request, user)
            request.session['email'] = request.data.get('email')
            request.session.save()
            token, _ = Token.objects.get_or_create(user=user)

            data = {
                'token': token.key
            }
            response = {
                'status': 'ok',
                'message': 'Usuario logeado correctamente',
                'data': data
            }
            return Response(response, status=status.HTTP_200_OK)
            
            #Tercer metodo de validacion
            refresh = RefreshToken.for_user(user)

            response_data = {
                'status': 'ok',
                'message': 'Usuario logeado correctamente',
                'data': {
                    'token': str(refresh.access_token),
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)
            
        else:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        '''

'''
http://127.0.0.1:8000/sivaria/v1/user/getCSRFToken

'''
@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):

    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'status': 'ok', 'message': 'Token creado correctamente'}, status=status.HTTP_200_OK)

'''
http://127.0.0.1:8000/sivaria/v1/user/deleteAccount

'''
class DeleteAccountView(APIView):

    def delete(self, request, format=None):
        user_service = UserService()
        try:
            user_service = UserService()
            email = request.data.get('email', None)
            try:
                email_clean = user_service.clean_email(email)
            except AttributeError as e:
                response = {
                    'status': 'error',
                    'message': 'Error obtetiendo los datos del usuario',
                    'data': str(e)
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
            user_service.delete_user(email=email_clean)
        except:
            return Response({'status': 'error', 'message': 'Error eliminando al usuario'}, status=status.HTTP_400_BAD_REQUEST)


'''
http://127.0.0.1:8000/sivaria/v1/user/logout

'''
class AppUser_APIView_Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        '''
        try:
            # Delete the user's token to logout

            #Primer metodo de logout
            request.user.auth_token.delete()
            response = {
                'status': 'ok',
                'message': 'Logout realizado correctamente',
            }
            return Response(response, status=status.HTTP_200_OK)
       
            #Segundo metodo de logout
            logout(request)
            Session.objects.filter(session_key=request.session.session_key).delete()
            response = {
                'status': 'ok',
                'message': 'Logout realizado correctamente',
            }
            return Response(response, status=status.HTTP_200_OK)

            #Tercer metodo de logout
            refresh_token = request.data.get('refresh_token')

            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)  # 205 Reset Content

        except Exception as e:
            return Response({'status':'error','message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        '''
        try:
            #logout(request)    
            request.user.auth_token.delete()
            response = {
                'status': 'ok',
                'message': 'Logout realizado correctamente'
            }
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'error', 'message': 'Error durante el proceso de logout'}, status=status.HTTP_400_BAD_REQUEST)

'''
Get info of a user by user Id
http://127.0.0.1:8000/sivaria/v1/user/{userId}

'''
class AppUser_APIView_Detail_UserId(APIView):
    
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (SessionAuthentication, )

    def get(self, request, userId, format=None):
        #userService = UserService()
        #user = userService.get_user_by_userId_json(userId)
        serializer = AppUserSerializer(data=request)
        user = serializer.data
        user.pop('password', None)
        response = {
            'status': 'ok',
            'message': 'Datos obtenidos correctamente',
            'data': user
        }
        return Response(response, status=status.HTTP_200_OK) 

'''
Get user data by user email

http://127.0.0.1:8000/sivaria/v1/getUserByEmail

'''
class AppUser_APIView_Detail_Email(APIView):

    def get(self, request, email, format=None):
        user_service = UserService()
        user_service.validate_email(email)
        try:
            email_clean = user_service.clean_email(email)
        except AttributeError as e:
            response = {
                'status': 'error',
                'message': 'Error obtetiendo los datos del usuario',
                'data': str(e)
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
        #email = request.get.data('email')
        user_has_parent_service = UserHasParentService()
        #print(email)
        user = user_service.get_user_by_email_json(email_clean)
        try: 
            user_has_parent = user_has_parent_service.get_user_has_parent_by_son_json(user['id'])
        except Exception as e:
            pass
        user.pop('password', None)
        user.pop('expo_token', None)

        rol = user.get('rol', None)
        if rol: 
            slug = rol.get('slug', None)
            if slug == 'joven':
                user['email_parent_1'] = user_has_parent.get('email_parent_1', None)
                user['email_parent_2'] = user_has_parent.get('email_parent_2', None) 
                responsible_id = user_has_parent.get('responsible', None)
                responsible = user_service.get_user_by_userId_json(responsible_id)
                user['responsible'] = (None if not responsible 
                                       else (
                                           responsible.get('first_name') + ' ' + responsible.get('last_name') + 
                                           ' - ' + responsible.get('email', None)
                                           ))
            elif slug == 'padre' or slug == 'madre':
                #print(user)
                user_has_parent_registers = user_has_parent_service.get_children_by_email_parent(email=user.get('email'))
                #print(children)
                children = []
                '''
                children_emails = []
                for user in children:
                    child = user_service.get_user_by_userId_json(children.id)
                    children_emails.append(child.get('email', ''))
                ''' 
                for user_has_parent_register in user_has_parent_registers:
                    children.append(user_has_parent_register.child.first_name + ' ' + user_has_parent_register.child.last_name + ' ('+ user_has_parent_register.child.code +')')
                user['children'] = ','.join(children)
            elif slug == 'profesional':
                professional_id = user.get('id')
                user_has_parent_registers=user_has_parent_service.get_children_by_responsible(responsible_id=professional_id)
                assigned_children = []
                for user_has_parent_register in user_has_parent_registers:
                    assigned_children.append(user_has_parent_register.child.first_name + ' ' + user_has_parent_register.child.last_name + ' ('+ user_has_parent_register.child.code +')')
                user['to_user'] = ','.join(assigned_children)

        titles = {
            'email': 'Email',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'phone': 'Teléfono',
            'birth_date': 'Fecha de nacimiento', 
            'email_parent_1': 'Email pariente 1',
            'email_parent_2': 'Email pariente 2',
            'responsible': 'Profesional asignado',
            'rol': 'Rol',
            'children': 'Hijos',
            'to_user': 'Pacientes asignados',
        }

        data = []
        for key in user:
            value = user.get(key, None)
            title = titles.get(key, None)
            if title:
                if key != 'rol':
                    #print(value)
                    #value = value if key != 'birth_date' else value.strftime('%d/%m/%Y')
                    if key == 'birth_date' and value:
                        year, month, day = value.split('-')
                        value = day + '/' + month + '/' + year
                    
                    singleData = {
                        'title': title,
                        'value': None if not value or value == '' else value,
                        'key': key,
                    }
                else:
                    singleData = {
                        'title': title,
                        'value': None if not value or value == '' else value['description'],
                        'key': str(key) + '_description',
                    }
                
                data.append(singleData)

        response = {
            'status': 'ok',
            'message': 'Datos obtenidos correctamente',
            'data': data
        }
        return Response(response, status=status.HTTP_200_OK) 


'''
Get user data by user email

http://127.0.0.1:8000/sivaria/v1/user/getUserByEmail/{email}

'''
class AppUser_APIView_Detail_Email_Api(APIView):

    def get(self, request, email, format=None):
        user_service = UserService()
        user_service.validate_email(email)
        try:
            email_clean = user_service.clean_email(email)
        except AttributeError as e:
            response = {
                'status': 'error',
                'message': 'Error obtetiendo los datos del usuario',
                'data': str(e)
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
        user = user_service.get_user_by_email_json(email_clean)

        response = {
            'status': 'ok',
            'message': 'Datos obtenidos correctamente',
            'data': user
        }
        return Response(response, status=status.HTTP_200_OK) 

'''
Update user data or delete user

http://127.0.0.1:8000/sivaria/v1/user/email/{email}

'''
class AppUser_APIView_Modifications(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, email, format=None):
        try:
            user_service = UserService()
            user_service.validate_email(email)
            try:
                email_clean = user_service.clean_email(email)
            except AttributeError as e:
                response = {
                    'status': 'error',
                    'message': 'Error eliminando al usuario',
                    'data': str(e)
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
             
            user = user_service.get_user_by_email(email_clean)
            user.delete()
            response = {
                'status': 'ok',
                'message': 'Usuario eliminado correctamente'
            }
            return Response(response, status=status.HTTP_200_OK) 
        except:
            return Response({'status': 'error', 'message': 'Error eliminando los datos del usuario'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, email, format=None):
        try:
            user_service = UserService()
            user_service.validate_email(email)
            try:
                email_clean = user_service.clean_email(email)
            except AttributeError as e:
                raise Exception(str(e)) 

            data = {}
            first_name = request.data.get('first_name', None)
            last_name = request.data.get('last_name', None)
            phone = request.data.get('phone', None)
            password = request.data.get('password', None)
            confirm_password = request.data.get('confirm_password', None)

            if first_name:
                data['first_name'] = first_name
            if last_name:
                data['last_name'] = last_name
            if phone:
                data['phone'] = phone
            if password and confirm_password and (password == confirm_password):
                data['password'] = make_password(password)
            
            user = user_service.get_user_by_email(email_clean)
            serializer_response, saved = user_service.update_user(user, data, partial=True)
            if saved:
                response = {
                    'status': 'ok',
                    'message': 'Datos actualizados correctamente',
                    'data': serializer_response
                }
                return Response(response, status=status.HTTP_200_OK) 
            else:
                raise Exception(serializer_response)
            '''
            user = AppUser.objects.get(email=email)
            serializer = AppUserSerializer(user, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            '''
        except Exception as e:
            error_message = str(e)
            return Response({'status': 'error', 'message': 'Error actualizando los datos del usuario. ' + error_message}, status=status.HTTP_400_BAD_REQUEST)

'''
Update user data or delete user

http://127.0.0.1:8000/sivaria/v1/user/{email}/changeUserPassword
{
    "password": string,
    "confirm_password": string
}
Note: the token is deleted once the password is changed
'''
class AppUser_APIView_Modifications_ChangePassword(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, email, format=None):
        try:
            user_service = UserService()
            user_service.validate_email(email)
            try:
                email_clean = user_service.clean_email(email)
            except AttributeError as e:
                response = {
                    'status': 'error',
                    'message': 'Error actualizando los datos del usuario',
                    'data': str(e)
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST) 

            password = request.data.get('password', None)
            confirm_password = request.data.get('confirm_password', None)
            
            if not password:
                raise Exception('El campo de la contraseña está vacío')
            if not confirm_password:
                raise Exception('El campo de confirmación de contraseña está vacío')
            if password and confirm_password and password != confirm_password:
                raise Exception('Las dos contraseñas no coinciden.')
            
            data = {}

            if password and confirm_password and (password == confirm_password):
                data['password'] = make_password(password)

            user = user_service.get_user_by_email(email_clean)
            serializer_response, saved = user_service.update_user(user, data, partial=True)
            if saved:
                response = {
                    'status': 'ok',
                    'message': 'Contraseña cambiada correctamente',
                    'data': serializer_response
                }
                
                #request.user.auth_token.delete()
                return Response(response, status=status.HTTP_200_OK) 
            else:
                raise Exception(serializer_response)
        except Exception as e:
            error_message = str(e)
            return Response({'status': 'error', 'message': 'Error actualizando los datos del usuario. ' + error_message}, status=status.HTTP_400_BAD_REQUEST)


'''
http://127.0.0.1:8000/sivaria/v1/expertSystem/predict
{
    "email": string,
    "user_data_sivaria": json string base64 decoded
}
'''
class ExpertSystem_APIView_Predict(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):

        '''
        Debe hacer 3 cosas.
        1. Guardar los datos del cuestionario en BBDD (OK)
        2. Realizar predicción (OK)
        3. Establecer las acciones dependiendo del tipo de riesgo devuelto de la predicción. (OK)
        '''
        response = {
            'status': 'error',
            'message': 'Error en la predicción'
        }
        expert_system_service = ExpertSystemService()
        user_service = UserService()
        rol_service = RolService()
        email_service = EmailService()
        email_template_service = EmailTemplateService()
        push_notification_type_service = PushNotificationTypeService()
        expo_service = ExpoService()
        user_has_parent_service = UserHasParentService()

        email = request.data.get('email', None)
        user_data_sivaria = request.data.get('user_data_sivaria', None)

        if not email:
            response['data'] = 'Email no especificado.'
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 
        
        if not user_data_sivaria:
            response['data'] = 'Datos del cuestionario no encontrado.'
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 

        try:
            user = user_service.get_user_by_email_json(email=email)
        except Exception as e:
            error_message = str(e)
            response['data'] = error_message
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 

        rol = user.get('rol' , None)

        if not rol:
            response['data'] = 'El usuario no tiene ningún rol'
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 

        rol_slug = rol.get('slug')
        
        #GUARDAR DATOS EN BBDD (DENTRO DE LA FUNCIÓN)
        
        #DECODIFICAR Y MAPEAR DATASET RECIBIDO DEL APP
        sivaria_mapping = True
        
        decoded_bytes = base64.b64decode(user_data_sivaria)
        json_str = decoded_bytes.decode('utf-8')
        sivaria_data_decoded = json.loads(json_str)

        form_instance, expert_system_json = ((None, sivaria_data_decoded) if not sivaria_mapping 
                                             else expert_system_service.map_data(user, sivaria_data_decoded, rol_slug))
        #print(form_instance)
        #PREDICCION

        model_type = ''
        if rol_slug == 'joven':
            model_type = 'autoinforme'
        elif rol_slug == 'madre' or rol_slug == 'padre':
            model_type = 'familia'
        elif rol_slug == 'profesional':
            model_type = 'profesional'

        if model_type.lower() not in ['autoinforme', 'familia', 'profesional']:
            response['data'] = 'Tipo de modelo '+ model_type +' no encontrado.'
            return Response(response, status=status.HTTP_404_NOT_FOUND) 
        
        json_encoded = base64.b64encode(json.dumps(expert_system_json).encode('utf-8'))
        desenlace = expert_system_service.predict(model_type, json_encoded)
        
        serializer = None
        if rol_slug == 'joven':
            serializer = YoungFormSerializer(form_instance, data={'prediction': desenlace}, partial=True)
        elif rol_slug == 'madre' or rol_slug == 'padre':
            serializer = FamilyFormSerializer(form_instance, data={'prediction': desenlace}, partial=True)
        elif rol_slug == 'profesional':
            serializer = ProfessionalFormSerializer(form_instance, data={'prediction': desenlace}, partial=True)
        
        if serializer.is_valid():
            serializer.save()
        
        #return 'HOLA'
            
        '''
        # Decoding data

        json_str = base64.b64decode(user_data_sivaria)
        print(json_str)

        new_data = json.loads(json_str.decode('utf-8'))
        print(new_data)

        newDF = pd.json_normalize(new_data)
        print(newDF)
        '''

        #ACCIONES DEL USUARIO (MANDAR EMAIL O PUSH A PROFESIONALES Y PADRES)
        #ENVIANDO PUSH A LOS PROFESIONALES
        # and (desenlace == 'IDEACION' or desenlace == 'AUTOLESION' or desenlace == 'PLANIFICACION' or desenlace == 'INTENCION')
        if desenlace:
            rol = rol_service.get_rol_by_slug_json(slug='profesional')
            rolId = rol.get('id', None)
            #print(rolId)
            #professionals = user_service.get_all_users_by_rol(rol=rolId)
            #print(professionals)

            code = None
            if desenlace == 'NINGUNO':
                code = 'riesgo_leve'
            elif desenlace == 'AUTOLESION':
                code = 'riesgo_moderado'
            elif desenlace == 'IDEACION':
                code = 'riesgo_moderado'
            elif desenlace == 'PLANIFICACION':
                code = 'riesgo_grave'
            elif desenlace == 'INTENCION':
                code = 'emergencia'

            code_professional = code + '_profesional'

            push_template = push_notification_type_service.get_push_notification_type_by_slug_json(slug=code_professional)
            email_template = email_template_service.get_email_template_by_code_json(code=code_professional)

            # ENVIO DE EMAIL Y PUSH AL PROFESIONAL ASIGNADO. DEPENDIENDO DE QUIEN COMPLETO EL CUESTIONARIO
            to_mail = []
            expo_tokens = []
            '''
            for professional in professionals:
                to_mail.append(professional.get('email', None))
                expo_tokens.append(professional.get('expo_token', None))
            '''
            email_professional = None
            email_parent_1 = None
            email_parent_2 = None
            email_professional = None
            expo_token_parent_1 = None
            expo_token_parent_2 = None

            if rol_slug == 'joven':
                userId = user.get('id',None)
                user_has_parent = user_has_parent_service.get_user_has_parent_by_son_json(child_id=userId)
                responsible_id = user_has_parent.get('responsible', '')
                professional = user_service.get_user_by_userId_json(responsible_id)

                email_parent_1 = user_has_parent.get('email_parent_1', None)
                if email_parent_1:
                    parent_1 = user_service.get_user_by_email_json(email_parent_1)
                    expo_token_parent_1 = parent_1.get('expo_token', None)

                email_parent_2 = user_has_parent.get('email_parent_2', None)
                if email_parent_2:
                    parent_2 = user_service.get_user_by_email_json(email_parent_2)
                    expo_token_parent_2 = parent_2.get('expo_token', None)
                
                email_professional = professional.get('email', None)
                expo_token_professional = professional.get('expo_token', None)

            elif rol_slug == 'padre' or rol_slug == 'madre':
                step1 = sivaria_data_decoded.get('step1', None)
                child_code = step1.get('idChild', None)
                child = user_service.get_user_by_code_json(child_code)
                child_id = child.get('id')
                user_has_parent = user_has_parent_service.get_user_has_parent_by_son_json(child_id)
                responsible_id = user_has_parent.get('responsible', '')
                professional = user_service.get_user_by_userId_json(responsible_id)

                email_parent_1 = user_has_parent.get('email_parent_1', None)
                if email_parent_1:
                    parent_1 = user_service.get_user_by_email_json(email_parent_1)
                    expo_token_parent_1 = parent_1.get('expo_token', None)

                email_parent_2 = user_has_parent.get('email_parent_2', None)
                if email_parent_2:
                    parent_2 = user_service.get_user_by_email_json(email_parent_2)
                    expo_token_parent_2 = parent_2.get('expo_token', None)

                email_professional = professional.get('email', None)
                expo_token_professional = professional.get('expo_token', None)

            elif rol_slug == 'profesional':
                step1 = sivaria_data_decoded.get('step1', None)
                child_code = step1.get('idPatient', None)
                child = user_service.get_user_by_code_json(child_code)
                child_id = child.get('id')
                user_has_parent = user_has_parent_service.get_user_has_parent_by_son_json(child_id)

                email_parent_1 = user_has_parent.get('email_parent_1', None)
                if email_parent_1:
                    parent_1 = user_service.get_user_by_email_json(email_parent_1)
                    expo_token_parent_1 = parent_1.get('expo_token', None)

                email_parent_2 = user_has_parent.get('email_parent_2', None)
                if email_parent_2:
                    parent_2 = user_service.get_user_by_email_json(email_parent_2)
                    expo_token_parent_2 = parent_2.get('expo_token', None)

                email_professional = user.get('email', None)
                expo_token_professional = user.get('expo_token', None)

            if email_professional:
                to_mail.append(email_professional)
            if expo_token_professional:
                expo_tokens.append(expo_token_professional)

            title = push_template.get('title' , None)
            message = push_template.get('body' , None)
            message = message.replace(r"{{desenlace}}", desenlace)
            #print(to_mail)
            #email_service.send_email(to_mail=to_mail, subject='Correo de prueba SIVARIA', message='Mensaje de Prueba')
            expo_service.send_push_messages(expo_tokens=expo_tokens, title=title, message=message)
            
            subject = email_template.get('subject' , None)
            message = email_template.get('message' , None)
            message = message.replace(r"{{desenlace}}", desenlace)
            email_service.send_email(subject=subject, message=message, to_mail=to_mail)


            #ENVIANDO PUSH O CORREO (EN CASO DE QUE NO ESTEN LOGEADOS EN LA PLATAFORMA) A LOS PADRES
            code_parents = code + '_padres'
            push_template_parents = push_notification_type_service.get_push_notification_type_by_slug_json(slug=code_parents)
            email_template_parents = email_template_service.get_email_template_by_code_json(code=code_parents)
            
            #print(email_parent_1)
            #print(email_parent_2)
            to_mail = []
            to_push = []
            '''
            if rol_slug == 'joven':
                userId = user.get('id',None)
                user_has_parent = user_has_parent_service.get_user_has_parent_by_son_json(child_id=userId)
                email_parent_1 = user_has_parent.get('email_parent_1',None)
                email_parent_2 = user_has_parent.get('email_parent_2',None)

                if email_parent_1:
                    try:
                        # SI EL PADRE O MADRE ESTA REGISTRADO EN LA APLICACION, SE LE ENVIA UN PUSH AL MOVIL
                        parent_1 = user_service.get_user_by_email_json(email=email_parent_1)
                        expo_token = parent_1.get('expo_token', None)
                        to_push.append(expo_token)
                    except:
                        pass
                    finally:
                        # SI EL PADRE O LA MADRE NO ESTAN REGISTRADOS EN LA APLICACION, SE LE ENVIA UN EMAIL
                        to_mail.append(email_parent_1)

                if email_parent_2:
                    try:
                        # SI EL PADRE O MADRE ESTA REGISTRADO EN LA APLICACION, SE LE ENVIA UN PUSH AL MOVIL
                        parent_2 = user_service.get_user_by_email_json(email=email_parent_2)
                        expo_token = parent_2.get('expo_token', None)
                        to_push.append(expo_token)
                    except:
                        pass
                    finally:
                        # SI EL PADRE O LA MADRE NO ESTAN REGISTRADOS EN LA APLICACION, SE LE ENVIA UN EMAIL
                        to_mail.append(email_parent_2)
            elif rol_slug == 'madre' or rol_slug == 'padre':
                    try:
                        # SI EL PADRE O MADRE ESTA REGISTRADO EN LA APLICACION, SE LE ENVIA UN PUSH AL MOVIL
                        parent_expo_token = user.get('expo_token', None)
                        to_push.append(parent_expo_token)
                    except:
                        pass
                    finally:
                        # SI EL PADRE O LA MADRE NO ESTAN REGISTRADOS EN LA APLICACION, SE LE ENVIA UN EMAIL
                        parent_email = user.get('email', None)
                        to_mail.append(parent_email)
                
            elif rol_slug == 'profesional':
                try:
                    step1 = sivaria_data_decoded.get('step1', None)
                    child_code = step1.get('idChild', None)
                    child = user_service.get_user_by_code_json(child_code)
                    child_id = child.get('id')
                    user_has_parent = user_has_parent_service.get_user_has_parent_by_son_json(child_id)
                    email_parent_1 = user_has_parent.get('email_parent_1', '')
                    email_parent_2 = user_has_parent.get('email_parent_2', '')

                    parent_1 = user_service.get_user_by_email_json(email_parent_1)
                    parent_2 = user_service.get_user_by_email_json(email_parent_2)
                    
                    # SI EL PADRE O MADRE ESTA REGISTRADO EN LA APLICACION, SE LE ENVIA UN PUSH AL MOVIL
                    parent_1_expo_token = parent_1.get('expo_token', None)
                    parent_2_expo_token = parent_2.get('expo_token', None)
                    
                    to_push.append(parent_1_expo_token)
                    to_push.append(parent_2_expo_token)
                except:
                    pass
                finally:
                    # SI EL PADRE O LA MADRE NO ESTAN REGISTRADOS EN LA APLICACION, SE LE ENVIA UN EMAIL
                    to_mail.append(email_parent_1)                   
                    to_mail.append(email_parent_2)
            '''
            #print(to_push)
            #print(to_mail)

            if expo_token_parent_1:
                to_push.append(expo_token_parent_1)
            if expo_token_parent_2:
                to_push.append(expo_token_parent_2)

            if email_parent_1:
                to_mail.append(email_parent_1)
            if email_parent_2:
                to_mail.append(email_parent_2)

            if to_push:
                title = push_template_parents.get('title', None)
                message = push_template_parents.get('body', None)
                expo_service.send_push_messages(expo_tokens=to_push, title=title, message=message)
            if to_mail:
                subject = email_template_parents.get('subject', None)
                message = email_template_parents.get('message', None)
                email_service.send_email(subject=subject, message=message, to_mail=to_mail)

        response['status'] = 'ok'
        response['message'] = 'Predicción hecha correctamente'
        response['data'] = desenlace

        return Response(response, status=status.HTTP_200_OK) 

'''
http://127.0.0.1:8000/sivaria/v1/external/sendNotification

'''
class External_SendNotification(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        response = {
            'status': 'error',
            'message': 'Error en el envío de la notificación',
        }
        user_service = UserService()
        push_notification_type_service = PushNotificationTypeService()
        
        data = request.data
        email = data.get('email', [])
        emails = []
        if isinstance(email, list):
            for email_data in email:
                emails.append(email_data['email'])
        else:
            emails.append(email)

        expo_tokens = []
        for email in emails:
            try:
                user_data = user_service.get_user_by_email_json(email)
                expo_token = user_data.get('expo_token')
                if expo_token is not None:
                    expo_tokens.append(expo_token)
            except:
                continue
            
        #expo_tokens = []
        #expo_tokens.append(expo_token)
        notification_type = request.data.get('notification_type', None)
        if notification_type is None:
            response['data'] = 'Tipo de notificación no enviada'
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 
        try:
            notification_type_data = push_notification_type_service.get_push_notification_type_by_slug_json(notification_type)
        except:
            response['data'] = 'Notificación no encontrada'
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 
 

        expo_service = ExpoService()
        try:
            title = notification_type_data.get('title', '')
            body = notification_type_data.get('body', '')
            data = notification_type_data.get('data')
            if data == '':
                data = None

            invalid_tokens = expo_service.send_push_messages(
                expo_tokens= expo_tokens,
                title=title,
                message=body,
                data=data, 
            )   

            if invalid_tokens:
                for invalid_token in invalid_tokens:
                    users = user_service.get_users_by_expo_token(invalid_token)
                    for user in users:
                        user_service.update_user(user=user, data={'expo_token':None}, partial=True)
                
        except Exception as exc:
            response['data'] = str(exc)
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
            

        response['status'] = 'ok'
        response['message'] = 'Notificación enviada'
        return Response(response, status=status.HTTP_200_OK) 

'''
http://127.0.0.1:8000/sivaria/v1/email/sendEmail
{
    "to_mail": array,
    "subject": string,
    "message": string
}
'''
class EmailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            email_service = EmailService()
            to_mail = request.data.get('to_mail', None)
            subject = request.data.get('subject', None)
            message = request.data.get('message', None)

            if not to_mail:
                raise Exception('Campo to_mail no encontrado.')
            if not isinstance(to_mail, list):
                raise Exception('Formato incorrecto del to_mail. Debe ser un array.')

            if not subject:
                raise Exception('Campo subject no encontrado.')
            if not isinstance(subject, str):
                raise Exception('Formato incorrecto del subject. Debe ser un string.')
    
            if not message:
                raise Exception('Campo message no encontrado.')
            if not isinstance(message, str):
                raise Exception('Formato incorrecto del message. Debe ser un string.')
            #to_mail = ['aldairfmh2004@hotmail.com']
            #subject = 'Mensaje de prueba'
            #message = 'Este es un mensaje de Prueba desde DRF'
            
            email_service.send_email(subject=subject, message=message, to_mail=to_mail)
            return Response({'status': 'ok', 'message': 'Correo enviado con éxito'}, status=status.HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            return Response({'status': 'error', 'message': error_message}, status=status.HTTP_400_BAD_REQUEST)


'''
http://127.0.0.1:8000/sivaria/v1/email/sendRecoveryPasswordEmail
{
    "email": string
}
'''
class EmailRecoveryPasswordApiView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            email_service = EmailService()
            email_template_service = EmailTemplateService()
            user_service = UserService()
            email = request.data.get('email', None)

            if not email:
                raise Exception('Email no encontrado.')
            
            user_service.validate_email(email)

            user = user_service.get_user_by_email(email=email)
            
            code_email_template = 'recovery_password'
            email_template = email_template_service.get_email_template_by_code_json(code=code_email_template)
            subject = email_template.get('subject', None)
            message = email_template.get('message', None)

            baseURL = env('FRONTEND_SIVARIA_BASE_URL')
            #print(baseURL)
            token, _ = Token.objects.get_or_create(user=user)
            #print(token)
            message = message.replace(r"{{baseURL}}", baseURL)
            message = message.replace(r"{{token}}", str(token))
            message = message.replace(r"{{email}}", email)

            #print(message)
            #to_mail = ['aldairfmh2004@hotmail.com']
            #subject = 'Mensaje de prueba'
            #message = 'Este es un mensaje de Prueba desde DRF'
            
            email_service.send_email(subject=subject, message=message, to_mail=[email])
            return Response({'status': 'ok', 'message': 'Correo enviado con éxito'}, status=status.HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            return Response({'status': 'error', 'message': error_message}, status=status.HTTP_400_BAD_REQUEST)
        

'''
http://127.0.0.1:8000/sivaria/v1/forms/getFormsDT
{
    "email": <str:user_email>
}

'''
class Forms_APIView_GetFormsDT(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        user_service = UserService()
        form_service = FormService()

        response = {
            'status': 'error',
            'message': 'Error en la obtención de los registros',
        }
        #print(request.data)

        email = request.data.get('email', None)
        #print(email)
        
        try:
            user_service.validate_email(email)
        except:
            response['data'] = 'Email vacío'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            email_clean = user_service.clean_email(email)
        except AttributeError as e:
            response['data'] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        

        #rol_data = rol_service.get_rol_by_id_json(rolId)
        user = user_service.get_user_by_email_json(email=email_clean)
        forms = form_service.get_forms_by_user_DT(user)   
                
        #rol_service.get_rol_by_id_json(rol)

        response = {
            'status': 'ok',
            'message': 'Datos devueltos correctamente',
            'data': forms,
        }
        return Response(response, status=status.HTTP_200_OK) 
    
'''
http://127.0.0.1:8000/sivaria/v1/forms/getFormInfo
{
    "email": <str:user_email>,
    "code": <str: form_code>
}

'''
class Forms_APIView_GetFormInfo(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        rol_service = RolService()
        user_service = UserService()
        form_service = FormService()

        email = request.data.get('email', None)
        code = request.data.get('code', None)
        
        try:
            user_service.validate_email(email)
        except:
            response['data'] = 'Email vacío'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            email_clean = user_service.clean_email(email)
        except AttributeError as e:
            response['data'] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        

        #rol_data = rol_service.get_rol_by_id_json(rolId)
        user = user_service.get_user_by_email_json(email=email_clean)
        form_info = form_service.get_form_info(user, code)   
                
        #rol_service.get_rol_by_id_json(rol)

        response = {
            'status': 'ok',
            'message': 'Datos devueltos correctamente',
            'data': form_info,
        }
        return Response(response, status=status.HTTP_200_OK) 
