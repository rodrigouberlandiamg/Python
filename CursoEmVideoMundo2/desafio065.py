maior = 0
menor = 0
count = 0
media = 0
soma = 0
n = 0
sair = False
while sair != True:
    n = int(input('Entre com o numero: '))
    if count == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma = soma + n
    count += 1
    sair = str(input('Deseja sair [S/N]: ')).upper()
    if sair == 'S':
        sair = True
    elif sair == 'N':
        sair = False
    else:
        print('Opção inválida. Processo terminado.')
        sair = True
print("Foram informados {} numeros e a media é {:.2f}".format(count,soma/count))
print('O Maior numero é {} e o menor é {}'.format(maior,menor))
print('FIM')
