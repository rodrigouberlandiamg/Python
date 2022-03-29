nome = input('Qual é seu nome ?')
print('Pazer em te conhecer {:20}!'.format(nome))

n1 = int(input('valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma {}, \n o produto {} e a \n divisão é {:.2f}'.format(s,m,d),end=' ')
print('Divisão intera {} e potencia {}'.format(di,e))
