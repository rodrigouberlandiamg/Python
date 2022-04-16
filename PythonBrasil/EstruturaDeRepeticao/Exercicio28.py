# Faça um programa que calcule o valor total investido por um colecionador em sua coleção
# de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de
# CDs e o valor para em cada um.
cds = []
vr = []
media = 0
qtdecds = int(input('Entre com a quantidade de CDs comprados: '))
for i in range(1,qtdecds+1):
    cds.append(input(f'Entre com o nome do CD[{i}]: '))
    vr.append(float(input(f'Entre com o valor do CD[{i}]: ')))
    media += vr[i-1]
print('RELACAO DE CDS')
print(f'Quantidade de CDS: {i}')
print('RELAÇÃO DE CDS')
print('=======================')
print('CD           VR')
for i in range(0,qtdecds):
    print(f'{cds[i]}            {vr[i]}')
print(f'TOTAL VALOR: R${media}')
print(f'TOTAL MEDIA: R${media/i+1}')