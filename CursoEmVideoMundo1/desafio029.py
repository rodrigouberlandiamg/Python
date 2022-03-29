velocidade = float(input('Entre com a velociade do carro: '))
if velocidade > 80:
    print('Voce foi multado velociade {} km/h a multa aplicada é de R${:.2f}.'.format(velocidade,(velocidade-80)*7))
else:
    print('Tenha um bom dia.')
print('FIM')