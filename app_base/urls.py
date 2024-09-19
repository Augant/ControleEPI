from django.urls import path
from app_base.views import index

urlpatterns = [
    path('', index),  
    
]