# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#
#    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#    comprar apenas latas de 18 litros;
#    comprar apenas galões de 3,6 litros;
#    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
#    arredonde os valores para cima, isto é, considere latas cheias.
import math
galaomaior = 0
galaomenor = 0
area = float(input('Entre com o tamanho da area a ser pintada em m2: '))
qtdelitrosmetro = area/6
qtdelitrosmetro += ((qtdelitrosmetro*10)/100)
if qtdelitrosmetro <= 3.6:
    vr = 25
elif qtdelitrosmetro > 3.6 and qtdelitrosmetro < 18:
    galaomenor = qtdelitrosmetro/3.6
    vr = math.ceil(galaomenor) * 25
elif (qtdelitrosmetro % 18) > 3.6 and (qtdelitrosmetro % 18) < 18:
    galaomaior = qtdelitrosmetro / 18
    qtdelitrosmetromenor = qtdelitrosmetro % 18
    galaomenor = qtdelitrosmetromenor / 3.6
    vr = (math.ceil(galaomenor) * 25) + math.ceil(galaomaior-1)*80
else:
    galaomaior = qtdelitrosmetro / 18
    vr = math.ceil(galaomaior)*80
print(f'A quantidade de litros para pintar a area de {area} m2 é de {math.ceil(qtdelitrosmetro)} litro(s) no valor de R${vr} ')
print(f'Serão gastos {math.floor(galaomaior)} galão(ões) de 18 litros e {math.ceil(galaomenor)} de 3.6 litros sendo que o valor total será de R${vr}')