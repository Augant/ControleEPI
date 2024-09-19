from django.shortcuts import render

def cadastroUser(request):
    return render(request, "app_usuarios/cadastroUser.html")

# Create your views here.
def loginUser(request):
    return render(request, "app_usuarios/loginUser.html")




# Create your views here.
