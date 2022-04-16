# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#
#                          Até 5 Kg           Acima de 5 Kg
#    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
#    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#    porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara
#    o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o
#    tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações
#    da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a
#    pagar.
while True:
    print('           CARNES DIPONIVEIS - ACOUGUE TABAJARAS            ')
    print('                            Até 5 Kg           Acima de 5 Kg')
    print('   1- File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg')
    print('   2- Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg')
    print('   3- Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')
    tipo_carne = int(input('Selecione o tipo de Carne: '))
    if tipo_carne in (1,2,3):
        break
qtde_carne = float(input('Entre com a quantidade de carne em KG: '))
while True:
    tipo_pagto = int(input('Entre com o tipo de pagamento 1 - Cartão Tabajaras 2 - Outros: '))
    if tipo_pagto in (1,2):
        break
vr_desconto = 0
vr_compra = 0
vr_desconto = 0
vr_compra_desc = 0
if tipo_carne == 1 and qtde_carne <= 5:
    vr_compra = (qtde_carne*4.9)
elif tipo_carne == 2 and qtde_carne <= 5:
    vr_compra = (qtde_carne*5.9)
elif tipo_carne == 3 and qtde_carne <= 5:
    vr_compra = (qtde_carne*6.9)
elif tipo_carne == 1 and qtde_carne > 5:
    vr_compra = (qtde_carne*5.8)
elif tipo_carne == 2 and qtde_carne > 5:
    vr_compra = (qtde_carne*6.8)
elif tipo_carne == 3 and qtde_carne > 5:
    vr_compra = (qtde_carne*7.8)
vr_compra_desc = vr_compra
if tipo_pagto == 1:
    vr_desconto = (vr_compra * 0.05)
    vr_compra_desc = vr_compra - (vr_compra*0.05)
carne = ''
if tipo_carne == 1:
    carne = 'File Duplo'
elif tipo_carne == 2:
    carne = 'Alcatra'
elif tipo_carne == 3:
    carne = 'Picanha'
pagto_tipo = ''
if tipo_pagto == 1:
    pagto_tipo = 'Cartao Tabajaras'
else:
    pagto_tipo = 'Outros'
    # tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a
    # #    pagar.
print(f'=============== CUPOM FISCAL ===============')
print(f'ITEM .................. {carne}             ')
print(f'QUANTIDADE ............ {qtde_carne}        ')
print(f'TOTAL ................. R${vr_compra}       ')
print(f'TIPO PAGTO ............ {pagto_tipo}        ')
print(f'DESCONTO .............. R${vr_desconto}     ')
print(f'VALOR A PAGAR ......... R${vr_compra_desc}  ')