import random
escolha_pc = int(random.choice([1,2,3]))
escolha_sua = int(input('Entre com sua escolha 1 = PEDRA, 2 = PAPEL e 3 = TESOURA: '))
if escolha_sua == escolha_pc:
    print('EMPATOU')
elif escolha_pc == 1 and escolha_sua == 2:
    print('Voce ganhou !!! Parabens.')
elif escolha_pc == 1 and escolha_sua == 3:
    print('Voce perdeu !!!.')
elif escolha_pc == 2 and escolha_sua == 1:
    print('Voce perdeu.')
elif escolha_pc == 2 and escolha_sua == 3:
    print('Voce ganhou !!! Parabens.')
elif escolha_pc == 3 and escolha_sua == 1:
    print('Voce ganhou !!! Parabens.')
elif escolha_pc == 3 and escolha_sua ==2:
    print('Voce Perdeu.')
print('O computador escolheu {} e voce escolheu {}'.format(escolha_pc,escolha_sua))
print('FIM DE JOGO.')
texto = 'Texto'
