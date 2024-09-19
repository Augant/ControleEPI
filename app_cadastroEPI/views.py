from django.shortcuts import render

def cadastroEPI(request):
    return render(request, "app_cadastroEPI/cadastrarEPI.html")

# Create your views here.
def listarEPI(request):
    return render(request, "app_cadastroEPI/listarEPI.html")
