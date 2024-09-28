from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprestimo
from .forms import EmprestimoForm
from app_cadastroEPI.models import Epi
from django.utils import timezone

def verificar_quantidade(epi, quantidade):
    """Verifica se a quantidade desejada é suficiente e atualiza a quantidade disponível."""
    return quantidade <= epi.quantidade_disponivel

def atualizar_quantidade_epi(epi, quantidade):
    """Deduz a quantidade emprestada do EPI disponível."""
    epi.quantidade_disponivel -= quantidade
    epi.save()


def criar_emprestimo(request):
    success_message = None
    error_message = None
    form = EmprestimoForm()  # Inicializa o formulário fora do bloco if

    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            epi = emprestimo.epi

            # Verificando a quantidade disponível
            if verificar_quantidade(epi, emprestimo.quantidade):
                atualizar_quantidade_epi(epi, emprestimo.quantidade)
                emprestimo.save()
                success_message = 'Empréstimo cadastrado com sucesso!'
                form = EmprestimoForm()  # Reseta o formulário em caso de sucesso
            else:
                error_message = 'Quantidade não disponível.'
        else:
            error_message = 'Erro ao cadastrar o empréstimo. Verifique os dados inseridos.'

    # Passando as mensagens para o template
    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
        'now': timezone.now(),  # Passa a data atual
    }
    return render(request, 'app_emprestimos/cadastrar_emprestimos.html', context)


def listar_emprestimos(request):
    queryset = Emprestimo.objects.all()

    funcionario_query = request.GET.get('funcionario')
    epi_query = request.GET.get('epi')

    if funcionario_query:
        queryset = queryset.filter(usuario__nome_usuario__icontains=funcionario_query)

    if epi_query:
        queryset = queryset.filter(epi__nome_epi__icontains=epi_query)

    return render(request, 'app_emprestimos/listar_emprestimos.html', {'emprestimos': queryset})



def deletar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    if request.method == 'POST':
        # Atualize a quantidade disponível do EPI
        emprestimo.epi.quantidade_disponivel += emprestimo.quantidade
        emprestimo.epi.save()
        emprestimo.delete()
        return redirect('listar_emprestimos')

    return render(request, 'app_emprestimos/deletar_emprestimos.html', {'emprestimo': emprestimo})

def devolver_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    if request.method == 'POST':
        data_devolucao = request.POST.get('data_devolucao')

        # Converter a data de devolução para um objeto date
        data_devolucao = timezone.datetime.strptime(data_devolucao, '%Y-%m-%d').date()

        # Verificar se a data de devolução é menor que a data de empréstimo
        if data_devolucao < emprestimo.data_emprestimo:  # Remova o .date() aqui
            error_message = 'A data de devolução não pode ser anterior à data de empréstimo.'
            return render(request, 'app_emprestimos/devolver_emprestimos.html', {
                'emprestimo': emprestimo,
                'error_message': error_message,
            })

        # Defina a data de devolução como a data selecionada
        emprestimo.data_devolucao = data_devolucao
        emprestimo.save()
        
        # Atualize a quantidade disponível do EPI
        emprestimo.epi.quantidade_disponivel += emprestimo.quantidade
        emprestimo.epi.save()
        
        return redirect('listar_emprestimos')

    return render(request, 'app_emprestimos/devolver_emprestimos.html', {'emprestimo': emprestimo})