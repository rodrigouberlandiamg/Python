# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo

n = int(input('Entre com o n-ésimo termo: '))
proximo = 0
anterior = 0


for i in range(0,n):
    print(proximo,end=' ')
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo += 1