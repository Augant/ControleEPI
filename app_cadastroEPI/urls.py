from django.urls import path
from app_cadastroEPI.views import  cadastroEPI, listarEPI

urlpatterns = [
    path('cadastroEPI/', cadastroEPI),
    path('listarEPI/', listarEPI),
    
]