from email.policy import default
from turtle import width
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.tipos_de_classe import tipos_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa

class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', widget=DatePicker(), initial=datetime.today, disabled=True)
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida': 'Data de ida', 'data_volta': 'Data de volta', 'data_pesquisa': 'Data da Pesquisa',
         'informacoes': 'Informações', 'classe_viagem': 'Classe de Vôo'}
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }
   
class PessoasForms(forms.ModelForm):

    class Meta:
        model = Pessoa
        exclude = ['nome']

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        list_error = {}
        campo_tem_algum_numero(origem, 'origem', list_error)
        campo_tem_algum_numero(destino, 'destino', list_error)
        origem_e_destino_iguais(origem, destino, list_error)
        data_ida_maior_que_data_volta(data_ida, data_volta, list_error)
        data_ida_menor_que_data_hoje(data_ida, data_pesquisa, list_error)
        if list_error is not None:
            for erro in list_error:
                message_error = list_error[erro]
                self.add_error(erro, message_error)
        return self.cleaned_data