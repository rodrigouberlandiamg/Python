#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene
# os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
par = []
impar = []
for i in range(20):
    numero = int(input(f'Entre com um numero inteiro [{i}]: '))
    numeros.append(numero)

for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'Par: {par}')
print(f'Impar: {impar}')