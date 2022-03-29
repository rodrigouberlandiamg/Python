distancia = float(input('Entre com a distancia da viagem: '))
if distancia <= 200:
    print('Valor da passagem para {} km: R${:.2f}'.format(distancia,(distancia*0.50)))
else:
    print('Valor da passagem para {} km: R${:.2f}'.format(distancia,(distancia*0.45)))