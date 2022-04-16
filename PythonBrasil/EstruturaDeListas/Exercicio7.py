# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.

numeros = []
soma = 0
multiplicacao = 1
for i in range(5):
    numero = int(input(f'Entre com um numero inteiro [{i}]: '))
    numeros.append(numero)
    soma += numero
    multiplicacao *= numero

print(f'Numeros: {numeros}.')
print(f'Soma: {soma}.')
print(f'{multiplicacao}.')
