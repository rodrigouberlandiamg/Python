# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma
# ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
# informando ao usuário nas seguintes situações:
#
#     Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa
#     não deve fazer pedir os demais valores, sendo encerrado;
#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e
#     encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math
print('==============================')
print('RAIZ DE EQUAÇÃO DE 2 GRAU')
print('==============================')
a = float(input('Entre com o valor de A: '))
if a == 0:
    print('Programa Finalizado')
else:
    b = float(input('Entre com o valor de B: '))
    c = float(input('Entre com o valor de C: '))
    vr_raiz = (b**2-4*a*c)
    print(f'Valor para raiz: {vr_raiz}')
    if vr_raiz > 0:
        valor1 = -b + math.sqrt(vr_raiz)
        valor2 = -b - math.sqrt(vr_raiz)
        total1 = valor1 / 2 * a
        total2 = valor2 / 2 * a
        print(f'Valor encontrado 1: {total1}')
        print(f'Valor encontrado 2: {total2}')
    else:
        print('Delta negativo. Não pode continuar.')

