# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
numeros = 0
maior = 0
qtde_num = int(input('Entre com a quantidade de numeros que deseja descobrir qual o maior: '))
for i in range(0,qtde_num):
    while True:
        numeros = int(input(f'Entre com o numero [{i+1}]: '))
        if numeros >= 0 and numeros <= 1000:
            break
        else:
            print('ERRO: O numero deve ser entre 0 e 1000.')
    if numeros> maior:
        maior = numeros

print(f'O maior numero encontrado na lista foi {maior}')