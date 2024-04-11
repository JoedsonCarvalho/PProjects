from turtle import pen
from django.shortcuts import render
from passagens.forms import PassagemForms, PessoasForms

def index(request):
    form = PassagemForms()
    pessoa_form = PessoasForms()
    contexto = {'form': form, 'pessoa_form': pessoa_form}
    return render(request, 'index.html', contexto)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoasforms = PessoasForms(request.POST)
        if form.is_valid():            
            contexto = {'form': form, 'pessoa_form': pessoasforms}
            return render(request, 'minha_consulta.html', contexto)
        else:
            print('Form inválido')
            contexto = {'form': form, 'pessoa_form': pessoasforms}
            return render(request, 'index.html', contexto)