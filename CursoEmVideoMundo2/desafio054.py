import datetime
for c in range(0,7):
    ano_nasc = int(input('Entre com o ano de nascimento da pessoa: '))
    if (datetime.date.today().year - ano_nasc) >= 21:
        print('A pessoa [{}] é de MAIOR.'.format(c))
    else:
        print('A pessoa [{}] é de MENOR.'.format(c))