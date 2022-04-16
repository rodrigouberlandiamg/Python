# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras
# lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar
# 6 vezes antes de ser enforcado.
#
#     Digite uma letra: A
#     -> Você errou pela 1ª vez. Tente de novo!
#
#     Digite uma letra: O
#     A palavra é: _ _ _ _ O
#
#     Digite uma letra: E
#     A palavra é: _ E _ _ O
#
#     Digite uma letra: S
#     -> Você errou pela 2ª vez. Tente de novo!
import random
palavra_forca = ''
with open('c:/temp/forca.txt','r') as palavras:
    count_lines = 0
    for palavra in palavras:
        count_lines += 1
    linha_int = random.randint(0,count_lines-1)


with open('c:/temp/forca.txt', 'r') as palavras_:
    count_linha_palavra = 0
    for p in palavras_:
        if linha_int == count_linha_palavra:
            palavra_forca = p.replace('\n','').upper()
            break
        count_linha_palavra += 1

#print(linha_int)
#print(palavra_forca)
count_erro = 0
lista_palavra = []
pos = 0
while True:
    letra = str(input(f'Digite uma letra: '))[0].upper()
    #print(letra)
    letra_existe = 0
    if letra in palavra_forca:
        lista_palavra.append(letra)
        print('A palavra é: ',end=' ')
        for x in palavra_forca:
            if x in lista_palavra:
                letra_existe += 1
#                if letra_existe == 1:
                print(f'{x}',end= ' ')
            else:
                print('_',end=' ')
            #print('')
            #print(f'{letra_existe} - {len(palavra_forca)}')
            pos += 1
        print('')
        if letra_existe == len(palavra_forca):
            print('GANHOU !!!')
            break
    else:
        count_erro += 1
        print(f'Voce errou pela {count_erro}º vez. Tente novamente.')
    if count_erro == 7:
        print(f'Quantidade de tentativas alcançadas. PERDEU. Palavra é {palavra_forca}')
        break

