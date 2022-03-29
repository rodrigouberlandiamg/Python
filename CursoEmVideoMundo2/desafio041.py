import datetime
ano = int(input('Entre com o ano de nascimento do atleta: '))
idade = datetime.date.today().year - ano
if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade >14 and idade <= 19:
    print('Junior')
elif idade == 20:
    print('Senior')
elif idade > 20:
    print('Master')
print('FIM')