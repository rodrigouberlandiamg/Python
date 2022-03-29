print('FATORIAL')
n = int(input('Entre com um numero: '))
m = n - 1
calculo = 0
while m != 0:
    if calculo == 0:
        calculo = n * m
#        print('{} x {} = {}'.format(n, m, calculo))
    else:
        calculo = calculo * m
#    print('{} x {} = {}'.format(calculo, m, calculo))
    m -= 1
print('O {}!: {:.2f}'.format(n,calculo))
print('FIM')