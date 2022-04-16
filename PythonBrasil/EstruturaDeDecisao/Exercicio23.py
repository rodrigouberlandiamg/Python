# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.
while True:
    try:
        numero = float(input('Entre com um numero qualquer: '))
        if round(float(numero)) == float(numero):
            print(f'Este numero {numero} é inteiro.')
        else:
            print(f'Este numero {numero} não é inteiro.')
        break
    except Exception as e:
        print(f'Entre com um numero válido. Erro: {e.args}')