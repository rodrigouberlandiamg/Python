a = float(input('Entre com o lado A: '))
b = float(input('Entre com o lado B: '))
c = float(input('Entre com o lado C: '))
if a < b + c and b < a + c and c < a + b:
    print('PODE se formar um triangulo.')
else:
    print('NAO se formar um triangulo.')
'''
if (a + b) > c:
    verdade1 = 0
else:
    verdade1 = 1
if (a + c) > b:
    verdade2 = 0
else:
    verdade2 = 1
if (c + b) > a:
    verdade3 = 0
else:
    verdade3 = 1
if (verdade1+verdade2+verdade3) == 0:
    print('PODE se formar um triangulo.')
else:
    print('NÃO pode se formar um triangulo.')'''