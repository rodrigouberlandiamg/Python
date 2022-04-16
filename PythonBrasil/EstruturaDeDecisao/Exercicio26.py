# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de
#     litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#     calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
#     é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = int(input('Entre com os litros de combustivel adquirido: '))
while True:
    tipo_combustivel = input('Entre com o tipo de combustivel adquirido A - Alcool | G - Gasolina: ')[0]
    if tipo_combustivel in ('gGaA'):
        break
vr_alcool = 1.9
vr_gasoliva = 2.5
vr_compra = 0
if tipo_combustivel.upper() == 'A' and litros <= 20:
    vr_compra = (vr_alcool * litros) - ((vr_alcool * litros) * 0.3)
elif tipo_combustivel.upper() == 'A' and litros > 20:
    vr_compra = (vr_alcool * litros) - ((vr_alcool * litros) * 0.5)
elif tipo_combustivel.upper() == 'G' and litros <= 20:
    vr_compra = (vr_gasoliva * litros) - ((vr_gasoliva * litros) * 0.4)
elif tipo_combustivel.upper() == 'G' and litros > 20:
    vr_compra = (vr_gasoliva * litros) - ((vr_gasoliva * litros) * 0.6)
print(f'Valor total de R${vr_compra}')