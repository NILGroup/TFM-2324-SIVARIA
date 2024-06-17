from django.urls import path
from .views import *

app_name = 'sivaria'

urlpatterns = [
    path('v1/post', Post_APIView.as_view()),
    path('v1/post/<int:postId>', Post_APIView_Detail.as_view()),
    path('v1/rol', Rol_APIView.as_view()),
    path('v1/rol/<str:slug>', Rol_APIView_Detail_Slug.as_view()),
    path('v1/rol/<int:rolId>', Rol_APIView_Detail_RolId.as_view()),
    path('v1/user/register', AppUser_APIView_Register.as_view()),
    path('v1/user/login', AppUser_APIView_Login.as_view()),
    path('v1/user/<int:userId>', AppUser_APIView_Detail_UserId.as_view()),
    path('v1/user/getUserByEmail', AppUser_APIView_Detail_Email.as_view()),
]
