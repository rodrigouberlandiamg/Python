# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um
# par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11,
# você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada,
# isto é chamado de "craps" e você perdeu. Se, na primeira jogada,
# você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando
# os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de
# tirar este Ponto novamente.
import random

def roda_dado():
    return random.randint(2,12)

jogada = 1
ponto = 0
while True:
    opcao = str(input('Jogar Dado [S/N]: '))[0].upper()
    if not opcao in 'SN':
        print('Opção inválida.')
    elif opcao == 'N':
        break
    else:
        valor_dado = roda_dado()
        print(f'RESULTADO DO DADO: {valor_dado}')
        print(f'JOGADA: {jogada}')
        if valor_dado in [7,11]:
            if jogada != 1 and valor_dado == 7:
                print(f'Voce PERDEU !!!')
            else:
                print(f'Voce é um natural e GANHOU !!!')
        elif valor_dado in [2,3,12]:
            print(f'Voce é um craps e PERDEU !!!')
        elif valor_dado in [4, 5, 6, 8, 9, 10]:
            print(f'Este é seu ponto {valor_dado} !!!')
            if valor_dado == ponto:
                print(f'Voce GANHOU !!!')
            else:
                ponto = valor_dado
        jogada += 1
print('FIM DE JOGO !!!')