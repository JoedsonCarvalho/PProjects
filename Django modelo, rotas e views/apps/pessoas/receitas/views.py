#from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Receita
#from django.http import HttpResponse

def index(request):

    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados )
    #return HttpResponse('<h1>Receitas</h1> <h1>Bem-Vindo</h2>')

# that represent each letter of the alphabet.
def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }
    
    return render(request, 'receita.html', receita_a_exibir)


def buscar(request):
    list_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            list_receitas = list_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': list_receitas
    }

    return render(request, 'buscar.html', dados)