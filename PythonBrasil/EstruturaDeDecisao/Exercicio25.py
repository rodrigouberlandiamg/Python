# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?"
#     O programa deve no final emitir uma classificação sobre a
#     participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
#     deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#     Caso contrário, ele será classificado como "Inocente".

while True:
    try:
        pergunta1 = input(f'Telefonou para a vítima? [S/N]: ').upper()
        pergunta2 = input(f'Esteve no local do crime? [S/N]: ').upper()
        pergunta3 = input(f'Mora perto da vítima? [S/N]: ').upper()
        pergunta4 = input(f'Devia para a vítima? [S/N]: ').upper()
        pergunta5 = input(f'Já trabalhou com a vítima? [S/N]: ').upper()

        if pergunta1 in ('SN') and pergunta2 in ('SN') and pergunta3 in ('SN') and pergunta4 in ('SN') and pergunta5 in ('SN'):
            if pergunta2 == 'S':
                print('Suspeita.')
            elif pergunta3 == 'S' and pergunta4 == 'S':
                print('Cúmplice')
            elif pergunta5 == 'S':
                print('Assasino.')
            else:
                print('Inocente.')
            break
        else:
            print(f'Existe pergunta não respondida ou incorreta.')
    except Exception as e:
        print(f'Ocorreu erro: {e.args}')