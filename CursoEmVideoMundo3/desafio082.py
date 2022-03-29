valores = list()
valores_pares = list()
valores_impares = list()
while True:
    valores.append(int(input('Entre com um numero: ')))
    while True:
        opcao = str(input('Deseja outro [S/N]: '))
        if opcao in 'sSnN':
            break
        else:
            print('Opção Invalida.')
    if opcao in 'nN':
        break
#print(valores)
for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)
valores.sort()
valores_pares.sort()
valores_impares.sort()
print(f'Lista completa: {valores}')
print(f'Lista Pares: {valores_pares}')
print(f'Lista Impares: {valores_impares}')