# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
#
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?"
#     O programa deve no final emitir uma classificação sobre a
#     participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
#     ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#     Caso contrário, ele será classificado como "Inocente".

perguntas = {
    0 : 'Telefonou para a vítima?',
    1 : 'Esteve no local do crime?',
    2 : 'Mora perto da vítima?',
    3 : 'Devia para a vítima?',
    4 : 'Já trabalhou com a vítima?'
}
respostas = []
for x in range(len(perguntas)):
    while True:
        resp = str(input(f'{perguntas[x]} [S/N]: '))
        if resp[0] in 'SNsn':
            break

    respostas.append(resp[0].upper())
count = 0
for x in range(len(respostas)):
    if respostas[x] == 'S':
        count += 1

if count == 2:
    print('Suspeita')
elif count >= 3 and count <= 4:
    print('Cúmplice')
elif count == 5:
    print('Assassino')
else:
    print('Inocente')