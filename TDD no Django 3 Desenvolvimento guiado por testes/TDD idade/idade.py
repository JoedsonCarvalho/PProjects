
# três etapas básica do TDD red green and refact(escrever o teste, 
# escrever o código para ser aprovado e refatorar)
# sig da sigla TDD, test driven development
def descobrir_idade(ano_nascimento, ano):
    return ano - ano_nascimento

assert descobrir_idade(1991, 2050) == 59

print(descobrir_idade(1996, 2060))