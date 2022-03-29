n1 = float(input('Entre com o primeiro numero: '))
n2 = float(input('Entre com o segundo numero: '))
n3 = float(input('Entre com o terceiro numero: '))
if n1 >= n2:
    maior = n1
    menor = n2
else:
    menor = n1
    maior = n2
if maior < n3:
    maior = n3
if n3 < menor:
    menor = n3
print('O maior numero é {} e o menor é {}'.format(maior,menor))
