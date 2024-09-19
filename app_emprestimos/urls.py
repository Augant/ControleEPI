from django.urls import path
from app_emprestimos.views import  emprestimo, listarEmprestismo

urlpatterns = [
    path('emprestimo/', emprestimo),
    path('listarEmprestimo/', listarEmprestismo),
    
]