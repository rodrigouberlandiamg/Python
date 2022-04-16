# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores
# com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas
# brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana
# recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam
# salários nos seguintes intervalos de valores:
#
#     $200 - $299
#     $300 - $399
#     $400 - $499
#     $500 - $599
#     $600 - $699
#     $700 - $799
#     $800 - $899
#     $900 - $999
#     $1000 em diante
#
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer
# vários ifs aninhados.
faixa_comissao = {
    200: [0],
    300: [0],
    400: [0],
    500: [0],
    600: [0],
    700: [0],
    800: [0],
    900: [0],
    1000: [0]
}
vendas = []
vr_venda = 0
while True:
    vr_venda = float(input(f'Valor da venda (0=SAIR): '))
    if vr_venda == 0:
        break
    else:
        vendas.append(vr_venda)

print(vendas)
comissoes = []
commisao = 0

for x in vendas:
    commisao = (x-(x*0.9))+200
    commisao_venda = commisao + x
    comissoes.append(commisao)

print(comissoes)
for valor in comissoes:
    #print(valor)
    for x in faixa_comissao:
        #print(x)
        if valor > 999:
            #print(type(faixa_comissao))
            #print(faixa_comissao[1000])
            novo_valor = int(faixa_comissao[1000][0]) + 1
            faixa_comissao[1000][0] = novo_valor
            break
        elif valor >= x and valor <= x+99:
            #print(type(faixa_comissao))
            #print(faixa_comissao[int(str(valor)[0]) * 100])
            novo_valor = int(faixa_comissao[int(str(valor)[0]) * 100][0]) + 1
            faixa_comissao[int(str(valor)[0]) * 100][0] = novo_valor
print('Lista com a faixas de salario.')
print(faixa_comissao)