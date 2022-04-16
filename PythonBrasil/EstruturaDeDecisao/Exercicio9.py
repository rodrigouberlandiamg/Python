# Faça um Programa que leia três números e mostre-os em ordem decrescente.
for n in range(3):
    numero = float(input(f'Entre com um numero {n}: '))
    if n == 0:
        maior = numero
        menor = numero
        meio = numero
    if numero > maior:
        meio = maior
        maior = numero
    elif numero < menor:
        menor = numero

print(f'O Maior numero é o {maior} o menor numero é o {menor} e o numero do meio é o {meio}')