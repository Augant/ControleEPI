from django.shortcuts import render

def controleUser(request):
    return render(request, "app_usuarios/controleUser.html")

# Create your views here.
def loginUser(request):
    return render(request, "app_usuarios/loginUser.html")




# Create your views here.
