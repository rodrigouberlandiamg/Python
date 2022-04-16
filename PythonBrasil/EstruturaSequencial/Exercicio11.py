#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#
#    o produto do dobro do primeiro com metade do segundo .
#    a soma do triplo do primeiro com o terceiro.
#    o terceiro elevado ao cubo.

n1 = int(input('Entre com o 1 numero inteiro: '))
n2 = int(input('Entre com o 2 numero inteiro: '))
nr = float(input('Entre com um numero real: '))
print(f'o produto do dobro do primeiro com metade do segundo: {(n1*2)*(n2/2)}')
print(f'a soma do triplo do primeiro com o terceiro: {(n1*3)+nr}')
print(f'o terceiro elevado ao cubo: {nr**3}')