# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido
while True:
    try:
        dia_semana = int(input('Entre com o dia da semana 1 até 7: '))
    except Exception as erro:
        print(f'Entre com o dia correto da semana numerico correspondente. Erro ocorrido {erro}.')
        break
    if dia_semana == 1:
        print('Domingo')
        break
    elif dia_semana == 2:
        print('Segunda - Feira')
        break
    elif dia_semana == 3:
        print('Terça - Feira')
        break
    elif dia_semana == 4:
        print('Quarta - Feira')
        break
    elif dia_semana == 5:
        print('Quinta - Feira')
        break
    elif dia_semana == 6:
        print('Sexta - Feira')
        break
    elif dia_semana == 7:
        print('Sabado')
        break
    else:
        print('Dia Inválido não corresponde a semana de 1 até 7.')