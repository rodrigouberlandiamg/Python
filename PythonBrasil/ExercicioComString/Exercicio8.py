# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se
# feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos.
# Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o
# exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
# uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

palavra = str(input('Entre com o palavra: '))
palavra_invertida = ''
for x in range(1,len(palavra)+1):
    palavra_invertida = f'{palavra_invertida}{palavra[len(palavra)-x]}'

if palavra.upper() == palavra_invertida.upper():
    print('É palíndromo.')
else:
    print('Não é palíndromo.')