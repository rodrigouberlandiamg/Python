n = int(input('Entre com um numero para verificar seus primos: '))
count = 0
for c in range(1,n+1):
    if (n % c) == 0:
        print('{} é divisivel por {}.'.format(n,c))
        count = count + 1
if count == 2:
    print('O numero {} é PRIMO'.format(n))
else:
    print('O numero {} NAO E PRIMO.'.format(n))