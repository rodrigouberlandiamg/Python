# Desenha moldura. Construa uma função que desenhe um retângulo usando os
# caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas,
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores
# fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de
# forma elegante.

def desenha_retangulo(linha,coluna, caracter='*'):
    if linha < 1:
        linha = 1
    elif linha > 20:
        linha = 20
    if coluna < 1:
        coluna = 1
    elif coluna > 20:
        coluna = 20

    for x in range(linha):
        print(f'{caracter}',end=' ')
    print('')
    for x in range(coluna-2):
        print(f'{caracter}',end='')
        for y in range(coluna-2-(coluna-linha)):
            print(' ',end=' ')
        print(f' {caracter}')
    for x in range(linha):
        print(f'{caracter}',end=' ')

desenha_retangulo(30,30,'R')