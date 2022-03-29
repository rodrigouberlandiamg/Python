preco = float(input('Entre com o preço do produto: '))
tipo_pagto = int(input('Entre com o tipo de pagamento: 1 - Dinheiro / Cheque, 2 - Cartao Débito, 3 - Parcelado no cartão: '))
if tipo_pagto == 1:
    print('O valor do produto é de R${:.2f}'.format(preco-(preco*10/100)))
elif tipo_pagto == 2:
    print('O valor do produto é de R${:.2f}'.format(preco-(preco*5/100)))
elif tipo_pagto == 3:
    parcela = int(input('Entre com a quantidade de parcelas: '))
    if parcela <= 2:
        print('O valor do produto é de R${:.2f} e será dividido em {} parcelas de {:.2f}'.format(preco,parcela,(preco/parcela)))
    elif parcela >= 3:
        novo_preco = preco+(preco*20/100)
        print('O valor do produto corrigido é de R${:.2f} e será dividido em {} parcelas de {:.2f}'.format(novo_preco, parcela,(novo_preco / parcela)))
    else:
        print('Opção INVALIDA')
print('FIM')