# Valida e corrige número de telefone. Faça um programa que leia um número de telefone,
# e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
# O usuário pode informar o número com ou sem o traço separador.
#
#     Valida e corrige número de telefone
#     Telefone: 461-0133
#     Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#     Telefone corrigido sem formatação: 34610133
#     Telefone corrigido com formatação: 3461-0133
novo_tel = ''
telefone = str(input('Entre com o telefone: '))
for x in telefone:
    if x in '0123456789':
        novo_tel = f'{novo_tel}{x}'
if len(novo_tel) == 7:
    novo_tel = f'3{novo_tel}'
    tel_formatado = f'{novo_tel[:4]}-{novo_tel[4:8]}'
    print(f'Telefone formatado: {tel_formatado}')
elif len(novo_tel) == 8:
    tel_formatado = f'{novo_tel[:4]}-{novo_tel[4:8]}'
    print(f'Telefone formatado: {tel_formatado}')
elif len(novo_tel) < 7 or len(novo_tel) > 8:
    print('Telefone invalido.')
