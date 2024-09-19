from django.urls import path
from app_usuarios.views import  controleUser, loginUser

urlpatterns = [
    path('controleUser/', controleUser),
    path('loginUser/', loginUser),
    
]