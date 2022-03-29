a = float(input('Entre com o lado A: '))
b = float(input('Entre com o lado B: '))
c = float(input('Entre com o lado C: '))
if a < b + c and b < a + c and c < a + b:
    print('PODE se formar um triangulo.')
else:
    print('NAO se formar um triangulo.')
if a == b and b == c:
    print('Equilatero')
elif a == b or a == c or b == c:
    print('Isosceles')
elif a != b and b != c and a != c:
    print('Escaleno')
print('FIM')