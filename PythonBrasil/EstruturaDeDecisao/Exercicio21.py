# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do
# saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis
# serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#
#     Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
#     uma nota de 5 e uma nota de 1;
#     Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
#     quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = float(input('Valor do Saque: '))
resto = 0
notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0
if valor > 100 and valor <= 600:
    resto = valor % 100
    notas100 = round((valor / 100)-0.5)
#print(resto)
if resto >= 50 and resto < 100:
    notas50 = round((resto / 50)-0.5)
    resto = resto % 50
#print(resto)
if resto >= 10 and resto < 49:
    notas10 = round((resto / 10)-0.5)
    resto = resto % 10
#print(resto)
if resto >= 5 and resto < 10:
    notas5 = round((resto / 5)-0.5)
    resto = resto % 5
#print(resto)
if resto >= 1 and resto < 5:
    notas1 = round((resto / 1)-0.5)
    resto = resto % 1
print(resto)
if notas100 != 0:
    print(f'Caixa retirada de {notas100} Notas de R$100,00')
if notas50 != 0:
    print(f'Caixa retirada de {notas50} Notas de R$50,00')
if notas10 != 0:
    print(f'Caixa retirada de {notas10} Notas de R$10,00')
if notas5 != 0:
    print(f'Caixa retirada de {notas5} Notas de R$5,00')
if notas1 != 0:
    print(f'Caixa retirada de {notas1} Notas de R$1,00')
