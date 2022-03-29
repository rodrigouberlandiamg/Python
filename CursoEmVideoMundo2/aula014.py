'''for c in range(1,10):
    print(c)
print('FIM')

for c in range(1,3):
    n = int(input('Entre com um valor: '))
print('FIM')


c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

n = 1
r = 'S'
while r == 'S':
    n = int(input('Entre com um valor: '))
    r = str(input('Deseja continuar [S/N]: ')).upper()
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Entre com um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares.'.format(par,impar))