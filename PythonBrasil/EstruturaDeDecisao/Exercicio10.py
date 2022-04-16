# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
# "Valor Inválido!", conforme o caso.

while True:
    turno = input('Entre com o turno que voce estuda M = Matutino, V = Vespertino, N = Noturno: ').upper()[0]
    if turno == 'M':
        print(f'Bom dia !!!')
        break
    elif turno == 'V':
        print(f'Boa Tarde !!!')
        break
    elif turno == 'N':
        print(f'Boa Noite !!!')
        break
    else:
        print('Valor inválido !!!')
