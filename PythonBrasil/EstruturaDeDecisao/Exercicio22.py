# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).
while True:
    try:
        numero = int(input('Entre com um numero inteiro: '))
        if numero % 2 == 0:
            print(f'O numero {numero} é PAR.')
        else:
            print(f'O numero {numero} é IMPAR.')
        break
    except Exception as e:
        print(f'Entre com um numero inteiro válido. Erro: {e.args}')