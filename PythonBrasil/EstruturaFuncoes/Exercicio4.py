# Faça um programa, com uma função que necessite de um argumento. A função retorna o
# valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero
# ou negativo.

def verifica(num):
    if num <= 0:
        return 'N'
    else:
        return 'P'

print(verifica(50))
print(verifica(0))
print(verifica(-30))