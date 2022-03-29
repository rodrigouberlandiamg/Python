def ficha(nome='<desconhecido>', gols='0'):
    print(f'O jogador {nome} fez {gols}.')

n = str(input('Nome do Jogador: '))
g = str(input('Quantidade de gols: '))
if n == '' and g == '':
    ficha()
elif n == '' and g != '':
    ficha("<desconhecido>",g)
elif n != '' and g == '':
    ficha(n, "0")
