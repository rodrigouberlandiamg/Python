# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
# intervalo compreendido por eles.
num1 = int(input('Entre com um numero inteiro: '))
num2 = int(input('Entre com outro numero inteiro: '))
maior = 0
menor = 1
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
for x in range(menor+1,maior):
    print(x, end= ' ')