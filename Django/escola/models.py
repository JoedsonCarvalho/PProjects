from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Cursos(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel_do_curso = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self) -> str:
        return self.descricao