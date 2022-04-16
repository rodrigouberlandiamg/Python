# Faça um Programa que peça um número correspondente a um determinado ano e em seguida
# informe se este ano é ou não bissexto.
ano = int(input('Entre com o ano para calcular se é bissexto: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano de {ano} é bissexto.')
        else:
            print(f'O ano de {ano} NÃO é bissexto.')
    else:
        print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} NÃO é bissexto.')