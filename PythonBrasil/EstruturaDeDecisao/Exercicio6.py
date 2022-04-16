# Faça um Programa que leia três números e mostre o maior deles.
ultimonum = 0
for n in range(3):
    numero = float(input(f'Entre com o numero {n}: '))
    if numero > ultimonum:
        ultimonum = numero
print(f'O maior numero digitado foi: {ultimonum}')