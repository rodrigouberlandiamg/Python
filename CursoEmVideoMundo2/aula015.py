count = 1
'''while count <= 10:
    print(count, '...', end='')
    count += 1
print('Acabou')'''

'''while True:
    print(count,' - ', end='')
    count += 1'''

n = s = 0
count = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('Soma = {}'.format(s))
print(f'A soma vale {s}')
print('A soma vale %s ' % (s))

print(f'Salario {s:.2f}')