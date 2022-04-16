# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n = float(input('Entre com um numero qualquer: '))
if n < 0:
    print(f'O {n} é NEGATIVO.')
else:
    print(f'O {n} é POSITIVO.')