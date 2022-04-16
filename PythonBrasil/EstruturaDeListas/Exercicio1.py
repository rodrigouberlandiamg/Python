#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
lista = []
for i in range(5):
    item_lista = int(input('Entre com um numero inteiro: '))
    lista.append(item_lista)

for y in lista:
    print(f'Item: {y}')
