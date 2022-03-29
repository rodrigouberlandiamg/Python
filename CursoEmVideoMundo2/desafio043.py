peso = float(input('Entre com o seu peso: '))
altura = float(input('Entre com o sua altura: '))
massa_corporica = peso/(altura*altura)
print('Sua massa IMC é {:.2f}'.format(massa_corporica))
if massa_corporica < 18.5:
    print('Abaixo do peso.')
elif massa_corporica >= 18.5 and massa_corporica < 25:
    print('Peso ideal PARABENS !!!')
elif massa_corporica >= 25 and massa_corporica < 30:
    print('Sobrepeso')
elif massa_corporica >= 30 and massa_corporica < 40:
    print('Obesidade')
elif massa_corporica >= 40:
    print('Obesidade Morbida')
print('FIM')