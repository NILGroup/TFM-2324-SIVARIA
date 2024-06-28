from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from .serializers import *
from django.http import Http404, HttpResponseBadRequest
from .services.services import RolService, UserService, UserHasParentService, ExpoService, PushNotificationTypeService
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

from ..validators.validators import LoginValidator

from django.middleware.csrf import get_token

from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator


#from scripts.controller import Controller

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
@method_decorator(csrf_protect, name='dispatch')
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
            response['data'] = 'Petición vacía'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        #cambiarlo por el serializador
        #rol_slug = request.data.get('rol_slug', None)
        #rol_instance = Rol.objects.get(slug=rol_slug)
        rol_instance = rol_service.get_rol_by_slug(request.data.get('rol_slug', None))

        data = {
            'first_name': request.data.get('first_name', None),
            'last_name': request.data.get('last_name', None),
            'email': request.data.get('email', None),
            'password': request.data.get('password', None),
            'phone': request.data.get('phone', None),
            'rol': rol_instance,
            'expo_token': request.data.get('expo_token', None)
        }
        # Validate data, in this case, the serializar makes the validation job with is_valid function()
        # Email would be already validated by EmailField in model
        # Password will be validated by the validators set in AUTH_PASSWORD_VALIDATORS property in the settings.py file
        # Phone will be validated with a custom validator
        # The password will be checked in the model and hashed in the create_user function, called in the create function in the serializer

        # The user is saved in AppUser table
        #serializer_response, saved = userService.save_user(data)

        user = user_service.register_user(data=data)
        if(user and request.data.get('rol_slug', None) == 'joven'):
            #user = userService.get_user_by_email_json(data['email'])
            email_parent_1 = request.data.get('email_parent_1', None)
            email_parent_2 = request.data.get('email_parent_2', None)
            if email_parent_1 is None and email_parent_2 is None:
                response = {
                    'status': 'error',
                    'message': 'No phone parent number was provided'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            
            uhpData = {
                'son': user,
                'email_parent_1': email_parent_1,
                'email_parent_2': email_parent_2
            }

            _ = user_has_parent_service.insert_user_has_parent(data=uhpData)

            token, created = Token.objects.get_or_create(user=user)

            response = {
                'status': 'ok',
                'message': 'Usuario registrado correctamente',
                'token': token.key
            }

            return Response(response, status=status.HTTP_201_CREATED)
        
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
      
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
        data = {
            'email':request.data.get('email', None),
            'password': request.data.get('password', None)
        }
        try:
            LoginValidator().validate_email(data)
        except:
            response['data'] = 'Email vacío'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:  
            LoginValidator().validate_password(data)
        except:
            response['data'] = 'Contraseña vacía'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = user_service.check_user(data)
            #login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            expo_token = request.data.get('expo_token',None)
            if expo_token is not None or expo_token == '':
                user_service.update_user(user=user, data={'expo_token': expo_token}, partial=True)
            
            user_data = user_service.get_user_by_email_json(email=data['email'])
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
        try:
            email = request.data.get('email', None)
            UserService().delete_user(email=email)
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

    def get(self, request, format=None):
        email = request.get.data('email')
        userService = UserService()
        user = userService.get_user_by_email_json(email)
        user.pop('password', None)
        response = {
            'status': 'ok',
            'message': 'Datos obtenidos correctamente',
            'data': user
        }
        return Response(response, status=status.HTTP_200_OK) 

'''
Update user data

http://127.0.0.1:8000/sivaria/v1/user/{email}/updateUserData

'''
class AppUser_APIView_Update(APIView):

    def put(self, request, email, format=None):
        try:
            data = request.data
            user = AppUser.objects.get(email=email)
            serializer = AppUserSerializer(user, data=data, partial=True)
            serializer.save()
            response = {
                'status': 'ok',
                'message': 'Datos actualizados correctamente',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK) 
        except:
            return Response({'status': 'error', 'message': 'Error actualizando los datos del usuario'}, status=status.HTTP_400_BAD_REQUEST)

'''
http://127.0.0.1:8000/sivaria/v1/expertSystem/{modelType}/predict

'''
'''
class ExpertSystem_APIView_Predict(APIView):

    def post(self, request, format=None):
        controller = Controller()
        argc = []
        result = controller.execute(argc)
        response = {
            'status': 'ok',
            'message': 'Predicción hecha correctamente',
            'data': result
        }
        return Response(response, status=status.HTTP_200_OK) 

'''
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


