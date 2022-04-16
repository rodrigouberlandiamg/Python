# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene
# os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios,
# simulando os lançamentos dos dados.
import random
qtde_num = 6
qtde_jogadas = 100
jogadas = []
resultado = {}
for i in range(qtde_jogadas):
    jogadas.append(random.randint(1,qtde_num))

print(jogadas)
for i in range(qtde_num):
    resultado[i+1] = 0

for i in jogadas:
    resultado[i] = resultado[i] + 1

print(resultado)