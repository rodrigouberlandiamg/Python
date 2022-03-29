print('Soma de numeros IMPARES no intervalo de 1..500')
soma = 0
for c in range(1,500+1,2):
    if c % 3 == 0:
        soma = soma + c
        print('Soma de {} + {} = {}'.format(soma-c,c,soma))
print('Soma FINAL {}'.format(soma))
soma = 0

for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
print('A soma de todos os valores solicitados {}.'.format(soma))