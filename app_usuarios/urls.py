from django.urls import path
from app_usuarios.views import  controleUser, loginUser, listarUser

urlpatterns = [
    path('controleUser/', controleUser),
    path('loginUser/', loginUser),
    path('listarUser/', listarUser),
    
    
]