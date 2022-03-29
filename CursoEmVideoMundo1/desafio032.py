import datetime
ano = int(input('Entre com o ano (coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year # Pega o ano atual que esta na maquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto.')
else:
    print('Essse ano não é bissexto.')