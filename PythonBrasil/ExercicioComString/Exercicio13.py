# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar
# uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de
# palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis
# tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela,
# informando se o usuário ganhou ou perdeu o jogo.
import random
palavra_embaralhada = ''
with open('c:/temp/forca.txt','r') as palavras:
    count_lines = 0
    for palavra in palavras:
        count_lines += 1
    linha_int = random.randint(0,count_lines-1)


with open('c:/temp/forca.txt', 'r') as palavras_:
    count_linha_palavra = 0
    for p in palavras_:
        if linha_int == count_linha_palavra:
            palavra_original = p.replace('\n','').upper()
            break
        count_linha_palavra += 1

lista_pos = random.sample(range(0, len(palavra_original) ), len(palavra_original))
#print(lista_pos)
print('Palavra misturada: ',end=' ')
for i in lista_pos:
    print(f'{palavra_original[i]}',end='')

print('')
count_erro = 0
for a in range(6):
    acha_palavra = str(input('Entre com sua palavra: '))
    if acha_palavra.upper() == palavra_original.upper():
        print('Voce ACERTOU.')
        break
    else:
        print(f'Voce ERROU a tentativa {count_erro+1} de 6.')
        count_erro += 1
        if count_erro == 6:
            print(f'Voce ERROU a palavra certa é {palavra_original}')
            break

print('FIM')
