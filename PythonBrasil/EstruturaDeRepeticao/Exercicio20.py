# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
# várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
while True:
    while True:
        numero = int(input('Entre com um numero inteiro: '))
        if numero > 0 and numero <= 16:
            break
        else:
            print('ERRO: Entre com numeros entre 1 e 16.')
    f = 1
    i = 0
    while i < numero:
        i += 1
        f = (i*f)
    print(f'{numero}! = {f}')
    while True:
        op = input(f'Deseja outro [S/N]: ')
        if op[0].upper() in ('SN'):
            break
        else:
            print('ERRO: Entre com a opção "S" para SIM e "N" para não.')
    if op[0].upper() == 'N':
        print('Programa FINALIZADO.')
        break