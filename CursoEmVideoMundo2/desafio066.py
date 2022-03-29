soma = 0
count = 0
n = 0
while True:
    n = int(input('Entre com o numero [Digite 999 para Sair]: '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'Foram informados {count} numeros e a soma deles é {soma}')