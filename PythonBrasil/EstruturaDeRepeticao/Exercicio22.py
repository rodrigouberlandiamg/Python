# Altere o programa de cálculo dos números primos, informando, caso o número não
# seja primo, por quais número ele é divisível.
numero = int(input('Entre com um numero inteiro: '))
count = 0
numeros = []
for i in range(1,numero+1):
    if numero % i == 0:
        numeros.append(i)
        count += 1
print(f'Existem {count} possíbilidade de divisão para este numero {numero}. Sendo assim: ')
if count == 2:
    print(f'O numero {numero} é PRIMO')
else:
    print(f'O numero {numero} NÃO é PRIMO ele pode ser divisivel por estes numeros {numeros}')