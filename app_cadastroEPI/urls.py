from django.urls import path
from .views import criar_epi, listar_epi, atualizar_epi, deletar_epi

urlpatterns = [
    path('cadastrar_epi/', criar_epi, name='criar_epi'),
    path('listar_epi/', listar_epi, name='listar_epi'),
    path('atualizar_epi/<int:id>/', atualizar_epi, name='atualizar_epi'),
    path('deletar_epi/<int:id>/', deletar_epi, name='deletar_epi'),
]
