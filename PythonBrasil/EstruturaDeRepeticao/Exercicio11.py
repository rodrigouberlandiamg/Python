# Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input('Entre com um numero inteiro: '))
num2 = int(input('Entre com outro numero inteiro: '))
maior = 0
menor = 1
soma = 0
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
for x in range(menor+1,maior):
    print(x, end= ' ')
    soma += x
print(f'A soma final dos numeros é {soma}')