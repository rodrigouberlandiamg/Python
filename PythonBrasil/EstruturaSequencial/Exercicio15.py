#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
'''    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido. '''
ganhohora = float(input('Entre com o valor ganho por hora R$: '))
horastrabalhadas = float(input('Entre com a quantidade de horas trabalhadas no mês: '))
print(f'SALARIO BRUTO: R${ganhohora*horastrabalhadas}')
print(f'IR (11%): R${(ganhohora*horastrabalhadas)*11/100}')
print(f'INSS (8%): R${(ganhohora*horastrabalhadas)*8/100}')
print(f'SINDICATO (5%): R${(ganhohora*horastrabalhadas)*5/100}')
print(f'SALARIO LIQUIDO: R${(ganhohora*horastrabalhadas)-((ganhohora*horastrabalhadas)*5/100)-((ganhohora*horastrabalhadas)*8/100)-((ganhohora*horastrabalhadas)*11/100)}')