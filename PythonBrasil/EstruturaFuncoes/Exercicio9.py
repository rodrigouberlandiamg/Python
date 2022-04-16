# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo: 127 -> 721

def reverso(num):
    str_num = str(num)
    lista = []
    novo = ''
    for i in str_num:
        lista.append(int(i))
    #print(lista)
    for i in reversed(lista):
        novo = f'{novo}{i}'
    return novo


print(reverso(127))