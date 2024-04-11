import abc

CONSTANTE = 10
idade = 18

for x in range(0, 100):
    print(x)


class Pessoa(abc.ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def diminuir_idade(self):
        self.idade -= 1

    def get_nome(self):
        return self.nome


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
        self.raca = "Humana"


a = Pessoa("Renan", 28)
funcionario1 = Funcionario("Renan", 28, 1000)

print(funcionario1.nome)

