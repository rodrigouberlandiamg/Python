# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
# lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas
# acima da média anual, e em que mês elas ocorreram (mostrar o mês por
# extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperatura = []
mes = {'0': 'Janeiro',
       '1': 'Fevereiro',
       '2': 'Março',
       '3': 'Abril',
       '4': 'Maio',
       '5': 'Junho',
       '6': 'Julho',
       '7': 'Agosto',
       '8': 'Setembro',
       '9': 'Outubro',
       '10': 'Novembro',
       '11': 'Dezembro'}
media_temp = 0
soma_temp = 0

for x in range(12):
    temp_mes = float(input(f'Entre com a temperatura média do mes de {mes[f"{x}"]}: '))
    temperatura.append(temp_mes)
    soma_temp += temp_mes

media_temp = soma_temp/len(temperatura)
for i in range(12):
    if temperatura[i] > media_temp:
        print(f'A temperatura {temperatura[i]} referente ao mês de {mes[f"{i}"]} foi maior que a média anual de {media_temp}')