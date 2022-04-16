# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
numero = int(input('Entre com um numero inteiro: '))
count = 0
for i in range(1,numero+1):
    if numero % i == 0:
        count += 1
print(f'Existem {count} possíbilidade de divisão para este numero {numero}. Sendo assim: ')
if count == 2:
    print(f'O numero {numero} é PRIMO')
else:
    print(f'O numero {numero} NÃO é PRIMO')