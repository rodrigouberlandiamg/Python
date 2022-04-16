#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = []
media = 0
for i in range(1,5):
    notas.append(float(input(f'Entre com a nota [{i}]: ')))
print(f'A media da soma das notas {notas} é igual a {sum(notas)/i}.')