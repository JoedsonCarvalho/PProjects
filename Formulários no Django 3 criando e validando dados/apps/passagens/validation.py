def origem_e_destino_iguais(origem, destino, list_erro):
    """Verifica se dois campos são iguais."""
    if origem == destino:
            list_erro['destino'] = 'Origem e destino não podem ser iguais.' 

def campo_tem_algum_numero(valor_campo, nome_campo, list_erro):
    """Verifica se o campo tem algum número."""
    if any(char.isdigit() for char in valor_campo):
        list_erro[nome_campo] = 'Não inclua números nesse campo.' 

def data_ida_maior_que_data_volta(data_ida, data_volta, list_error):
    """Verifica se a data de ida é maior que a data de volta."""
    if data_ida > data_volta:
        list_error['data_volta'] = "Data de ida não pode ser maior que a data de volta."

def data_ida_menor_que_data_hoje(data_ida, data_pesquisa, list_error):
    """Verifica se a data de ida é menor que a data atual/hoje."""
    print(data_ida, data_pesquisa)
    print(type(data_ida))
    print(type(data_pesquisa))
    if data_ida < data_pesquisa:
        list_error['data_ida'] = "A data de ida não pode ser menor que a data de hoje."