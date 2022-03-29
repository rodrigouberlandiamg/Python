import random
count = 0
sair = False
while sair != True:
    count += 1
    numero = int(input('Entre com um numero: '))
    numero_pc = random.randint(0,10)
    if numero == numero_pc:
        print('Acertou miseravel...')
        sair = True
    else:
        print('Erro miseravel...')
        sair = False
print('Foram feita(s) {} tentativa(s) até voce ganhar o jogo.'.format(count))
