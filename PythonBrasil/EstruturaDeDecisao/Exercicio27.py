# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#
#                          Até 5 Kg           Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#
#    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
#    receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a
#    quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser
#    pago pelo cliente.

morango = float(input('Entre com a quantidade de morango adquirido em KG: '))
maca = float(input('Entre com a quantidade de maça adquirido em KG: '))
vr_tot_morango = 0
vr_tot_maca = 0

if morango < 5:
    vr_tot_morango = (morango*2.5)
else:
    vr_tot_morango = (morango*2.2)
if morango < 5:
    vr_tot_maca = (maca*2.2)
else:
    vr_tot_maca = (maca*1.5)
print(f'O Valor dos morangos foi de R${vr_tot_morango} e os da maça foi de R${vr_tot_maca} somando um total de R${vr_tot_maca+vr_tot_morango}')