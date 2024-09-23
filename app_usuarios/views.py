from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

def listar_usuarios(request):
    if (query := request.GET.get('q')):
        usuarios = Usuario.objects.filter(nome_usuario__icontains=query)
    else:
        usuarios = Usuario.objects.all()
    
    return render(request, 'app_usuarios/listar_usuarios.html', {'usuarios': usuarios})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'app_usuarios/cadastrar_usuario.html', {'form': form})

def atualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'app_usuarios/atualizar_usuario.html', {'form': form, 'usuario': usuario})

def confirmar_deletar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    
    return render(request, 'app_usuarios/confirmar_deletar_usuario.html', {'usuario': usuario})
