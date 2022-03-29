import random
'''s = 'a'
volta = True
win = louse = 0
while volta == True:
    soma = 0
    valida = True
    n = int(input('Informe o valor: '))
    while valida == True:
        s = str(input('Selecione par [P] ou impar [I]: ')).upper()
        if s[0] == 'P':
            valida = False
        elif s[0] == 'I':
            valida = False
        else:
            valida = True
    soma = n + random.randint(0,10)
    #print(soma)
    if soma % 2 == 0:
        if s[0] == 'P':
            print('VOCE GANHOU ...')
            win += 1
            break
        else:
            print('VOCE PERDEU ...')
            louse += 1
            volta = True
    else:
        if s[0] == 'I':
            print('VOCE GANHOU ...')
            win += 1
            break
        else:
            print('VOCE PERDEU ...')
            louse += 1
            volta = True
print(f'Voce ganhou {win} vezes e perdeu {louse} vezes para o computador.')
print('FIM')'''
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Ganhou !!!')
            v += 1
        else:
            print('Voce Perdeu !!!')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('Voce Ganhou !!!')
            v += 1
        else:
            print('Voce Perdeu !!!')
            break
    print('Vamos jogar novamente !!!')
print('FIM')