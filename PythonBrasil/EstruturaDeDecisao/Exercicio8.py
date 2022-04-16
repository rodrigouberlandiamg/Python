# Faça um Programa que leia três números e mostre o maior e o menor deles.
for n in range(3):
    numero = float(input(f'Entre com um numero {n}: '))
    if n == 0:
        menor = numero
        maior = numero
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
print(f'O menor numero encontrado foi: {menor} e o maior foi: {maior}')