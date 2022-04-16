#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
# tinta a serem compradas e o preço total.
import math
area = float(input('Entre com o tamanho da area a ser pintada em m2: '))
qtdelitrosmetro = area/3
if qtdelitrosmetro <= 3.6:
    vr = 25
elif qtdelitrosmetro > 3.6 and qtdelitrosmetro < 18:
    galaomenor = qtdelitrosmetro/3.6
    vr = math.ceil(galaomenor) * 25
else:
    galaomaior = qtdelitrosmetro/18
    vr = math.ceil(galaomaior)*80
print(f'A quantidade de litros para pintar a area de {area}m2 é de {qtdelitrosmetro} litro(s) no valor de R${vr} ')