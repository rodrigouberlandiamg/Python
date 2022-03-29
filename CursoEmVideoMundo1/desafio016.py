import math
n = float(input('Entre com um numero real: '))
print('A porção inteira de {} é igual a {}'.format(n,int(n)))
print('A porção inteira de {} é igual a {:.0f}'.format(n,math.trunc(n)))
