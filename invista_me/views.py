from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


def investimentos(request):
    # retornando todos os objetos da tabela investimento do banco de dados
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)


def detalhe(request, id_investimento):
    # retornando o id no bando de dados
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)


@login_required
def criar(request):
    # Enviando dados através do POST (Atualizando formulario)
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        # Verificando se esta valido
        if investimento_form.is_valid():
            # salvando no bando de dados
            investimento_form.save()
        return redirect('investimentos')
    else:
        # Criando formulario do zero
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    # novo_investimento/1 -> GET
    if request.method == 'GET':
        # Preenchendo o formulario com os dados ja enviados
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    else:
        # caso a requisição seja POST
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')


@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})
