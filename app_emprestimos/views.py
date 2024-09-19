from django.shortcuts import render

def emprestimo(request):
    return render(request, "app_emprestimos/emprestimo.html")

# Create your views here.
def listarEmprestismo(request):
    return render(request, "app_emprestimos/listarEmprestimo.html")


# Create your views here.
