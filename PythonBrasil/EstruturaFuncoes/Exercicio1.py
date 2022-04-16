# Faça um programa para imprimir:
#
#         1
#         2   2
#         3   3   3
#         .....
#         n   n   n   n   n   n  ... n
#
#     para um n informado pelo usuário. Use uma função que receba um valor n inteiro e
#     imprima até a n-ésima linha.

def gera_num(num):
    numero = 0
    for i in range(num):
        numero += 1
        num_str = f'{str(numero)} '
        print(f'{num_str * (i + 1)}')

gera_num(10)