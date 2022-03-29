count = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Entre com o numero: '))
    if n == 999:
        print('Sair')
    else:
        soma = soma + n
        count += 1
print("Foram informados {} e a soma é {}".format(count,soma))
