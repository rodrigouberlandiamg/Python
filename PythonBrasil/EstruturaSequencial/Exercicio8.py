#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês
ganhohora = float(input('Entre com o valor que ganha por hora: R$'))
horatrab = float(input('Entre com a quantidade de horas trabalhadas por mes: '))
salario = ganhohora*horatrab
print(f'Voce ganha por mês R${salario} por mês.')