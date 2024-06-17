from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from .serializers import *
from django.http import Http404, HttpResponseBadRequest
from .services.services import RolService, UserService, UserHasParentService
# User authentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import generics, permissions

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

    serializer_class = RolSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        rolService = RolService()
        rols = rolService.get_all_rols_json()
        response = {
            'status': 'ok',
            'message': 'Datos devueltos correctamente',
            'data': rols
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
class AppUser_APIView_Register(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        rolService = RolService()
        userHasParentService = UserHasParentService()
        userService = UserService()

        data = {
            'name': request.data.get('name', None),
            'surname': request.data.get('surname', None),
            'email': request.data.get('email', None),
            'password': userService.hash_password(request.data.get('password', None)),
            'phone': request.data.get('phone', None),
            'id_rol': request.data.get('rolId', None)
        }
        print(data)
        # The user is saved in AppUser table
        serializer_response, saved = userService.save_user(data)
        if saved:
            id_rol = data['id_rol']
            rol = rolService.get_rol_by_id_json(id_rol)

            if(rol['slug'] == 'joven'):
                # pillar numeros de los padres.
                user = userService.get_user_by_email_json(data['email'])

                uhpData = {
                    'id_son': user['id'],
                    'phone_parent_1': request.data.get('phone_parent_1', None),
                    'phone_parent_2': request.data.get('phone_parent_2', None)
                }

                serializer_response, saved = userHasParentService.save_user_has_parent(uhpData)
                if saved:
                    response = {
                        'status': 'ok',
                        'message': 'Usuario registrado correctamente' 
                    }
                    return Response(response, status=status.HTTP_201_CREATED)

        
        response = {
            'status': 'error',
            'message': 'Error en el registro del usuario',
            'data': serializer_response
        }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)

'''
http://127.0.0.1:8000/sivaria/v1/user/login

'''
class AppUser_APIView_Login(APIView):

    permission_classes = [permissions.AllowAny]


    def post(self, request, format=None):
        userService = UserService()
        
        data = {
            'email': request.data.get('email'),
            'password': request.data.get('password')
        }

        response = {
            'status': 'error',
            'message': 'Credenciales inválidas'
        }
        '''
        try:
            user = userService.get_user_by_email_json(data['email'])
        except (Http404, HttpResponseBadRequest) as e:
            response['data'] = e
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        verified = userService.verify_password(data['password'], user['password'])
        '''
        user = authenticate(username=data['email'], password=data['password'])
        if user:
            print('\n' + 'Creando el token' + '\n')
            token, _ = Token.objects.get_or_create(user=user)

            response['status']='ok'
            response['message']='Usuario logeado correctamente'
            response['data'] = {
                'token': token.key
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

'''
http://127.0.0.1:8000/sivaria/v1/user/logout

'''
class AppUser_APIView_Logout(APIView):

    def post(self, request, format=None):
        userService = UserService()

        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'status':'ok', 'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':'ok','message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


'''
Get info of a user by user Id
http://127.0.0.1:8000/sivaria/v1/user/{userId}

'''
class AppUser_APIView_Detail_UserId(APIView):
    
    def get(self, request, userId, format=None):
        userService = UserService()
        return Response(userService.get_user_by_userId_json(userId)) 

'''
Get user by user email

http://127.0.0.1:8000/sivaria/v1/getUserByEmail

'''
class AppUser_APIView_Detail_Email(APIView):

    def get(self, request, format=None):
        email = request.get.data('email')
        userService = UserService()
        return Response(userService.get_user_by_email_json(email)) 
