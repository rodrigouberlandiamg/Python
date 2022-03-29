vr_casa = float(input('Entre com o valor da casa: '))
salario = float(input('Entre com o salario: '))
anos = int(input('Entre com a quantidade de anos a pagar: '))
vr_mensal = vr_casa / (anos * 12)
if vr_mensal > (salario*30/100):
    print('NEGADO, seu salario é inferior ao minimo necessário para o valor mensal de R${:.2f}.'.format(vr_mensal))
else:
    print('APROVADO o financiamento de R${:.2f} o valor da parcela é igual R${:.2f} em {} parcela(s)'.format(vr_casa,(vr_casa/(anos*12)),anos))
