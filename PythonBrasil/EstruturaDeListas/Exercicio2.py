#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
for i in range(10):
    item_lista = float(input('Entre com um numero real: '))
    lista.append(item_lista)
#lista.sort(reverse=True)
print(len(lista))
for y in range(10):
    print(f'Item: {lista[(len(lista)-1)-y]}')