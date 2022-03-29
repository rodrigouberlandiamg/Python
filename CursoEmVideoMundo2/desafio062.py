print('RAZAO')
op = 0
termo = int(input('Entre com o primeiro termo: '))
r = int(input('Entre com o Razao: '))
while op != 1:
    valor = 0
    n = 0
    while n < r:
        termo = termo + r
        print('Razão de [{}]: {}'.format(r,termo))
        n += 1
    r = int(input('Mais termos: '))
    if r == 0:
        op = 1
print('FIM')