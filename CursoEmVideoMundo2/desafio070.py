countprodmaior1000 = count = menorpreco = 0
nomeprodmaisbarato = ''
sair = naocadastrar = False
while sair == False:
    count += 1
    sair = naocadastrar = False
    nome = str(input('Entre com o nome do produto: '))
    preco = float(input('Entre com o valor do produto R$'))
    if preco > 1000.00:
        countprodmaior1000 += 1
    if count == 1:
        menorpreco = preco
    if preco < menorpreco:
        menorpreco = preco
        nomeprodmaisbarato = nome
    while naocadastrar == False:
        escolha = str(input('Deseja cadastrar outro [S/N]: ')).upper()
        if escolha[0] == 'S':
            naocadastrar = True
        elif escolha[0] == 'N':
            naocadastrar = True
        else:
            naocadastrar == False
    if escolha[0] == 'N':
        break
    else:
        sair = False
print(f'Existem {countprodmaior1000} produto(s) que custam mais de R$1000.00.')
print(f'O produto mais barato: {nomeprodmaisbarato}.')
