# Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input('Entre com um numero: '))
n2 = float(input('Entre com outro numero: '))
if n1 > n2:
    print(f'O primeiro numero digitado {n1} é maior que o {n2}.')
elif n1 == n2:
    print('São iguais.')
else:
    print(f'O segundo numero digitado {n2} é maior que o {n1}.')