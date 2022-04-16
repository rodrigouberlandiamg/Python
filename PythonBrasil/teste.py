maior = 0
menor = 0

for x in range(5):
    peso = float(input(f'Entre com o peso da pessoa {x}:'))
    if x == 0:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso


print(f'Maior: {maior}')
print(f'Menor: {menor}')