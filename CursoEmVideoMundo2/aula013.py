for c in range(0,6):
    print('{} - Oi'.format(c))
print('FIM')

for a in range(6,0,-1):
    print(a)
print('FIM')

n = int(input('Digite um numero: '))
for c in range(0,n+1):
    print(c)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i,f+1,p):
    print(c)
print('FIM')