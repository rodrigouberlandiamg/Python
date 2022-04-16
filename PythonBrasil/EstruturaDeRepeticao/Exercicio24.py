# Faça um programa que calcule o mostre a média aritmética de N notas.
qtde_notas = int(input('Entre com a quantidade de notas: '))
notas = 0
for i in range(1,qtde_notas+1):
    notas += float(input(f'Entre com a nota [{i}]: '))
print(f'A media foi de {notas/qtde_notas}')