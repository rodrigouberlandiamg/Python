# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada
# seja invertida.
#
#     FULANO
#     FULAN
#     FULA
#     FUL
#     FU
#     F

nome = str(input('Entre com o nome: '))

for x in range(0,len(nome)):
    print(f'{nome[0:len(nome)-x].upper()}')