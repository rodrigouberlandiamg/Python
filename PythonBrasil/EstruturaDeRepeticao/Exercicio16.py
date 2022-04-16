# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

#n = int(input('Entre com o n-ésimo termo: '))
proximo = 0
anterior = 0


while proximo < 500:
    print(proximo,end=' ')
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo += 1