# Faça um programa para imprimir:
#
#         1
#         1   2
#         1   2   3
#         .....
#         1   2   3   ...  n
#
#     para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima
#     até a n-ésima linha.


def gera_num(num):
    numero = 0
    for i in range(0,num):
        print('')
        for x in range(1,i+1):
            num_str = str(x)
            print(f'{num_str}',end=' ')

gera_num(100)