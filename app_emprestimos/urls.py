from django.urls import path
from .views import listar_emprestimos, criar_emprestimo, devolver_emprestimo, deletar_emprestimo

urlpatterns = [
    path('listar_emprestimos/', listar_emprestimos, name='listar_emprestimos'),
    path('cadastrar_emprestimos/', criar_emprestimo, name='cadastrar_emprestimo'),
     path('devolver_emprestimo/<int:emprestimo_id>/', devolver_emprestimo, name='devolver_emprestimo'),  
    path('deletar_emprestimo/<int:emprestimo_id>/', deletar_emprestimo, name='deletar_emprestimo'), 
]
