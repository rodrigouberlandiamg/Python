#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma
# dos quadrados dos elementos do vetor.

vetor_a = []
soma = 0
for i in range(10):
    num_quadrado = 0
    numero = int(input(f'Entre com o numero [{i}]: '))
    vetor_a.append(numero)
    num_quadrado = numero ** 2
    soma += num_quadrado
print(f'A soma do quadrado dos elementos {vetor_a} é de {soma}.')
