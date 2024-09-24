from django.urls import path
from .views import listar_usuarios, cadastrar_usuario, atualizar_usuario, confirmar_deletar_usuario, login_view

urlpatterns = [
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('atualizar_usuario/<int:id>/', atualizar_usuario, name='atualizar_usuario'),
    path('deletar_usuario/<int:id>/', confirmar_deletar_usuario, name='confirmar_deletar_usuario'),
    path('login/', login_view, name='login')
]
