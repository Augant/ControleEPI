from django.urls import path
from app_usuarios.views import  cadastroUser, loginUser

urlpatterns = [
    path('cadastroUser/', cadastroUser),
    path('loginUser/', loginUser),
    
]