valor = 0
termo = int(input('Entre com o Termo: '))
r = int(input('Entre com o Razao da PA: '))
n = 0
while n < 10:
    termo = termo + r
    print('Razão de [{}]: {} '.format(r,termo))
    n += 1
print('FIM')