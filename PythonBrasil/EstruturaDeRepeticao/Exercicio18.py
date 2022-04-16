# Faça um programa que, dado um conjunto de N números, determine o menor valor,
# o maior valor e a soma dos valores.

numeros = []
maior = 0
qtde_num = int(input('Entre com a quantidade de numeros que deseja descobrir qual o maior: '))
for i in range(0,qtde_num):
    numeros.append(int(input(f'Entre com o numero [{i+1}]: ')))
    if numeros[i] > maior:
        maior = numeros[i]
print('Lista os numeros:')
print(f'{numeros}')
print(f'O maior numero encontrado na lista foi {maior}')