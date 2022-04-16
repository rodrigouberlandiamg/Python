# Data com mês por extenso. Construa uma função que receba uma data no
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def data_extenso(data):
    lista_mes = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abrir',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    #print(data)
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:10]
    return f'{dia} de {lista_mes[int(mes)]} de {ano}.'

print(data_extenso('10/12/1980'))
