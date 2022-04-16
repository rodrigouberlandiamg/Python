# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1
# (que não deve ser armazenado). Após esta entrada de dados, faça:
#
#     Mostre a quantidade de valores que foram lidos;
#     Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#     Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#     Calcule e mostre a soma dos valores;
#     Calcule e mostre a média dos valores;
#     Calcule e mostre a quantidade de valores acima da média calculada;
#     Calcule e mostre a quantidade de valores abaixo de sete;
#     Encerre o programa com uma mensagem;
try:
    numeros = []
    while True:
        numero = float(input(f'Entre com as notas ou [-1] para sair: '))
        if numero == -1:
            break
        else:
            numeros.append(numero)

    print(f'Quantidade de numeros lidos: {len(numeros)}')
    print(f'Valores informados: {numeros}')
    print(f'Numeros na ordem inversa:')
    for i in range(len(numeros)):
        print(numeros[(len(numeros)-1)-i])
    soma = 0
    for x in numeros:
        soma += x
    print(f'Soma dos valores: {soma}')
    media = soma/len(numeros)
    print(f'A média dos valores é : {media}')
    icount_acima_media = 0
    icount_acima_7 = 0
    for i in numeros:
        if i > media:
            icount_acima_media += 1
        if i > 7:
            icount_acima_7 += 1
    print(f'Quantidade de numeros acima da media: {icount_acima_media}')
    print(f'Quantidade de numeros acima de 7: {icount_acima_7}')
finally:
    print(f'FIM DO SISTEMA')