# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário
# o valor da sua hora e a quantidade de horas trabalhadas no mês.
#
#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#
#             Salário Bruto: (5 * 220)        : R$ 1100,00
#             (-) IR (5%)                     : R$   55,00
#             (-) INSS ( 10%)                 : R$  110,00
#             FGTS (11%)                      : R$  121,00
#             Total de descontos              : R$  165,00
#             Salário Liquido                 : R$  935,00

vr_hora = float(input('Entre com o valor da hora do funcionario: R$ '))
horas_trab = int(input('Entre com a quantidade de horas trabalhadas no mês: '))
salario_bruto = vr_hora*horas_trab
if salario_bruto <= 900:
    ir = 'Isento'
    vr_ir = 0
    salario_liquido = salario_bruto
if salario_bruto > 900 and salario_bruto <= 1500:
    salario_liquido = salario_bruto - ((salario_bruto*5)/100)
    ir = 5
    vr_ir = (salario_bruto*5)/100
if salario_bruto > 1500 and salario_bruto <= 2500:
    salario_liquido = salario_bruto - ((salario_bruto*10)/100)
    ir = 10
    vr_ir = (salario_bruto * 10) / 100
if salario_bruto > 2500:
    salario_liquido = salario_bruto - ((salario_bruto * 20) / 100)
    ir = 20
    vr_ir = (salario_bruto * 20) / 100
print(f'Salario Bruto: ({horas_trab} * {vr_hora})   : R$ {salario_bruto}')
print(f'(-) IR ({ir}%):                 : R$ {vr_ir}')
print(f'(-) INSS (10%)               : R$ {salario_bruto*10/100}')
print(f'FGTS (11%)                   : R$ {salario_bruto*11/100}')
print(f'Total de descontos           : R$ {vr_ir+(salario_bruto*10/100)}')
print(f'Salario Liquido              : R$ {salario_liquido-(salario_bruto*10/100)}')