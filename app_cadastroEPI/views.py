from django.shortcuts import render, redirect, get_object_or_404
from .models import Epi
from .forms import EpiForm

def listar_epi(request):
    if (query := request.GET.get('q')):
        epis = Epi.objects.filter(nome_epi__icontains=query)
    else:
        epis = Epi.objects.all()
    
    return render(request, 'app_cadastroEPI/listar_epi.html', {'epis': epis})

def criar_epi(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        form = EpiForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "EPI cadastrado com sucesso!"
            form = EpiForm()  # Reseta o formulário após sucesso
        else:
            error_message = "Erro ao cadastrar o EPI. Verifique os dados inseridos."
    else:
        form = EpiForm()

    return render(request, 'app_cadastroEPI/cadastrar_epi.html', {
        'form': form,
        'success_message': success_message,
        'error_message': error_message
    })


def atualizar_epi(request, id):
    epi = get_object_or_404(Epi, id=id)
    if request.method == 'POST':
        form = EpiForm(request.POST, instance=epi)
        if form.is_valid():
            form.save()
            return redirect('listar_epi')
    else:
        form = EpiForm(instance=epi)

    return render(request, 'app_cadastroEPI/atualizar_epi.html', {'form': form, 'epi': epi})

def deletar_epi(request, id):
    epi = get_object_or_404(Epi, id=id)
    if request.method == 'POST':
        epi.delete()
        return redirect('listar_epi')
    
    return render(request, 'app_cadastroEPI/deletar_epi.html', {'epi': epi})
