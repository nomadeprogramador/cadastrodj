from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from .models import Funcionario
# Create your views here.
from .forms import FuncionarioForm

def editar_funcionario(request,id):
    funcionario= get_object_or_404(Funcionario,id=id)
    if request.method=='POST':
        funcionario = FuncionarioForm(request.POST,instance=funcionario)
        if funcionario.is_valid():
            funcionario.save()
            return redirect('funcionario:listar_funcionarios')
        else:
            return HttpResponse('Erro ao editar funcionario')
    funcionario = FuncionarioForm(instance=funcionario)
    context={
        'funcionario':funcionario
    }
    return render(request,'funcionario/editar.html',context)
    
def cadastrar_funcionario(request):
    if request.method =='POST':
        form =FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('funcionario:listar_funcionarios')
        return HttpResponse('Erro ao realizar o cadastro ')
    form = FuncionarioForm()
    context = {
        'form':form,
    }

    return render (request,'funcionario/cadastrar.html',context)


def listar_funcionarios (request):
    funcionarios = Funcionario.objects.all()
    context={
        'funcionarios':funcionarios,
    }
    return render(request,'funcionario/listar.html',context)


def detalhes_funcionario(request,id):
    funcionario = Funcionario.objects.get(id=id)
    context = {
        'funcionario':funcionario,
    }
    return render (request,'funcionario/detalhes.html',context)

def excluir_funcionario(request,id):
    funcionario = get_object_or_404(Funcionario,id=id)
    funcionario.delete()
    return redirect('funcionario:listar_funcionarios')
