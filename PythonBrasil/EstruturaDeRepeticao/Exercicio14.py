# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
# pares e a quantidade de números impares.
numero = 0
count_par = 0
count_impar = 0
for x in range(0,10):
    numero = int(input(f'Entre com o numero[{x}]: '))
    if numero % 2 == 0:
        count_par += 1
    else:
        count_impar += 1
print(f'Existem {count_par} numeros pares e {count_impar} numeros impares.')