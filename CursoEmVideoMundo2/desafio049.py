n = int(input('Entre com um numero intero de tabuada: '))
print('='*13)
for c in range(0,11):
    print('{} x {} = {}'.format(n,c,n*c))
print('FIM')