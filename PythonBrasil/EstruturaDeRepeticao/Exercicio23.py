# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
# fornecido pelo usuário. O programa deverá mostrar também o número de divisões que
# ele executou para encontrar os números primos. Serão avaliados o funcionamento,
# o estilo e o número de testes (divisões) executados.

numero = int(input('Entre com um numero inteiro: '))
count = 0
numeros = []
for i in range(1,numero+1):
    if numero % i == 0:
        print(f'Divisão relaizada: {numero} / {i} = {numero/i}')
        numeros.append(i)
        count += 1
print(f'Existem {count} possíbilidade de divisão para este numero {numero}. Sendo assim: ')
if count == 2:
    print(f'O numero {numero} é PRIMO ele pode ser divisivel por estes numeros {numeros}')
else:
    print(f'O numero {numero} NÃO é PRIMO ele pode ser divisivel por estes numeros {numeros}')