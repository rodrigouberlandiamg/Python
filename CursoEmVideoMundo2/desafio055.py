maior = 0
menor = 1000
for c in range(0,5):
    peso = float(input('Entre com o peso: '))
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior,menor))