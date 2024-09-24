from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprestimo
from .forms import EmprestimoForm
from app_cadastroEPI.models import Epi

def verificar_quantidade(epi, quantidade):
    """Verifica se a quantidade desejada é suficiente e atualiza a quantidade disponível."""
    return quantidade <= epi.quantidade_disponivel

def atualizar_quantidade_epi(epi, quantidade):
    """Deduz a quantidade emprestada do EPI disponível."""
    epi.quantidade_disponivel -= quantidade
    epi.save()

def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            epi = emprestimo.epi  # Acesso ao EPI relacionado

            # Verificando a quantidade
            if not verificar_quantidade(epi, emprestimo.quantidade):
                form.add_error('quantidade', 'Quantidade não disponível.')
                return render(request, 'app_emprestimos/cadastrar_emprestimos.html', {'form': form})

            # Atualizando a quantidade disponível do EPI
            atualizar_quantidade_epi(epi, emprestimo.quantidade)

            # Salvando o empréstimo
            emprestimo.save()
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm()

    return render(request, 'app_emprestimos/cadastrar_emprestimos.html', {'form': form})

def listar_emprestimos(request):
    queryset = Emprestimo.objects.all()

    funcionario_query = request.GET.get('funcionario')
    epi_query = request.GET.get('epi')

    if funcionario_query:
        queryset = queryset.filter(usuario__nome_usuario__icontains=funcionario_query)

    if epi_query:
        queryset = queryset.filter(epi__nome_epi__icontains=epi_query)

    return render(request, 'app_emprestimos/listar_emprestimos.html', {'emprestimos': queryset})

def devolver_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    if request.method == 'POST':
        # Defina a data de devolução como a data atual
        emprestimo.data_devolucao = request.POST.get('data_devolucao')
        emprestimo.save()
        # Atualize a quantidade disponível do EPI
        emprestimo.epi.quantidade_disponivel += emprestimo.quantidade
        emprestimo.epi.save()
        return redirect('listar_emprestimos')

    return render(request, 'app_emprestimos/devolver_emprestimos.html', {'emprestimo': emprestimo})


def deletar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    if request.method == 'POST':
        # Atualize a quantidade disponível do EPI
        emprestimo.epi.quantidade_disponivel += emprestimo.quantidade
        emprestimo.epi.save()
        emprestimo.delete()
        return redirect('listar_emprestimos')

    return render(request, 'app_emprestimos/deletar_emprestimos.html', {'emprestimo': emprestimo})