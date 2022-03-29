import datetime
ano = int(input('Entre com o ano do seu nascimento: '))
idade = datetime.date.today().year - ano
if idade < 18:
    print('Ainda vai se alistar daqui {} ano(s).'.format(18-idade))
elif idade == 18:
    print('Hora de se alistar')
elif idade > 18:
    print('Passou {} ano(s) do tempo de se alistar.'.format(idade-18))