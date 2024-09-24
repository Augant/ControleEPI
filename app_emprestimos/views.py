from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprestimo
from .forms import EmprestimoForm

def listar_emprestimos(request):
    queryset = Emprestimo.objects.all()

    funcionario_query = request.GET.get('funcionario')
    epi_query = request.GET.get('epi')

    if funcionario_query:
        queryset = queryset.filter(usuario__nome_usuario__icontains=funcionario_query)

    if epi_query:
        queryset = queryset.filter(epi__nome_epi__icontains=epi_query)

    return render(request, 'app_emprestimos/listar_emprestimos.html', {'emprestimos': queryset})



def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm()

    return render(request, 'app_emprestimos/cadastrar_emprestimos.html', {'form': form})
