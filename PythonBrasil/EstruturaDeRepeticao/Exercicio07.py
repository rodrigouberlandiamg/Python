# Faça um programa que leia 5 números e informe o maior número.
maior = 0
numero = 0
for x in range (0,5):
    numero = float(input(f'Entre com o numero [{x}]: '))
    if x == 0:
        maior =  numero
    if maior < numero:
        maior = numero
print(f'O maior numero digitado foi é {maior}.')