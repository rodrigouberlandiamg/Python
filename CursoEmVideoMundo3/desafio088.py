import random
from time import sleep
jogos = list()
numeros = list()
qtde_jogos = int(input('Entre com a quantidade de jogos: '))
'''for i in range(qtde_jogos):
    numeros.append(random.sample(range(1,61),6))
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
for i in range(len(jogos)):
     print(jogos[i])
'''
count = 0
for i in range(qtde_jogos):
    while True:
        num_gerado = random.randint(1,60)
        if num_gerado not in numeros:
            numeros.append(num_gerado)
            count += 1
            if count == 6:
                numeros.sort()
                jogos.append(numeros[:])
                numeros.clear()
                count = 0
                break

for i in range(len(jogos)):
     print(jogos[i])
     sleep(1)
