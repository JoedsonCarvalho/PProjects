from email.policy import default
from tkinter import CASCADE
from django.db import models
from datetime import datetime

from pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateField(default=datetime.now, blank=True)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_receita


    