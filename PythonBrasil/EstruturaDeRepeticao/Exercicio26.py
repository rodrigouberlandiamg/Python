# Numa eleição existem três candidatos. Faça um programa que peça o número total de
# eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Entre com o numedo de eleitores: '))
voto = 0
canditado1 = 0
canditado2 = 0
canditado3 = 0
for i in range(1,eleitores+1):
    print('Escolha o canditado\n1 - Canditado 1\n2 - Canditado 2\n3 - Canditado 3\n')
    while True:
        voto = int(input(f'Eleitor [{i}] opção de candidato: '))
        if voto > 0 and voto < 4:
            break
        else:
            print('Escolha um upção de voto entre 1 e 3.')
    if voto == 1:
        canditado1 += 1
    elif voto == 2:
        canditado2 += 1
    else:
        canditado3 += 1

print('RESULTADO DA ELEICAO:')
print(f'CANDIDATO 1: {canditado1}')
print(f'CANDIDATO 2: {canditado2}')
print(f'CANDIDATO 3: {canditado3}')