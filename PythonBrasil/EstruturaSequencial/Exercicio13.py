#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#
#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7
altura = float(input('Entre com sua altura: '))
print(f'Seu peso ideal para sexo masculino seria: {(72.7*altura) - 58}')
print(f'Seu peso ideal para sexo feminino seria: {(62.1*altura) - 44.7}')