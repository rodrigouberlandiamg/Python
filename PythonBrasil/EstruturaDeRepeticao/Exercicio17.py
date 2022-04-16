# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120
numero = int(input('Entre com um numero inteiro: '))
f = 1
i = 0
while i < numero:
    i += 1
    f = (i*f)
print(f'{numero}! = {f}')

