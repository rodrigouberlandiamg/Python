soma = 0
for c in range(0,6):
    n = int(input('Entre com o numero [{}]: '.format(c)))
    if n % 2 != 0:
        soma = soma+n
        print('Foi somado {} + {} = {}'.format(soma-n,n,soma))
print('A soma final é de : {}'.format(soma))