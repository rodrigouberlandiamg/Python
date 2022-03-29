n = int(input('Entre com um numero [1..1999]: '))
u = n // 1 % 10
c = n // 10 % 10
d = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {3}, Centena: {2}, Dezena: {1} e Milhar: {0}'.format(int(u),int(d),int(c),int(m)))
