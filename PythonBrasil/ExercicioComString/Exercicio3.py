# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#
#     F
#     U
#     L
#     A
#     N
#     O

nome = str(input('Entre com o nome: '))

for x in nome:
    print(f'{x.upper()}')