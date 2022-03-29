import math
a = float(input('Entre com um valor para calcular seno, coseno e tanjente: '))
b = math.radians(a)
print('O valor do seno {:.2f} do cosseno é {:.2f} e da tanjente é {:.2f}'.format(math.sin(b),math.cos(b),math.tan(b)))
