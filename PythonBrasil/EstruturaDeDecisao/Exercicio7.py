# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
# comprar, sabendo que a decisão é sempre pelo mais barato.
ultimonum = 0
for n in range(3):
    numero = float(input(f'Entre com o valor do produto {n}: '))
    if n == 0:
        ultimonum = numero
    if numero < ultimonum:
        ultimonum = numero
print(f'O menor valor do produto encontrado foi: R${ultimonum}')