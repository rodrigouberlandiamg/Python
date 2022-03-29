n1 = int(input('Entre com o primeiro numero: '))
n2 = int(input('Entre com o segundo numero: '))
if n1 > n2:
    print('Primeiro valor é maior {}'.format(n1))
elif n2 > n1:
    print('Segundo valor é maior {}'.format(n2))
elif n1 == n2:
    print('Os dois valores são iguais {}'.format(n1))
print('FIM')