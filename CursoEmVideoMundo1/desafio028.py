import random
numero = int(input('Entre com um numero: '))
numero_pc = random.randint(0,5)
if numero == numero_pc:
    print('Acertou miseravel...')
else:
    print('Erro miseravel.')
print('O numero escolhido pelo computador é {}, e voce digitou {}'.format(numero_pc,numero))
