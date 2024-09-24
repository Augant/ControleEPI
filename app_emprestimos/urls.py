from django.urls import path
from .views import listar_emprestimos, criar_emprestimo

urlpatterns = [
    path('listar_emprestimo/', listar_emprestimos, name='listar_emprestimos'),
    path('cadastrar_emprestimo/', criar_emprestimo, name='cadastrar_emprestimo'),
]