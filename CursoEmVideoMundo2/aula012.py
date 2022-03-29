nome = str(input('Qual é seu nome: '))
#print('Tenha um bom dia {}'.format(nome))
if nome == 'Rodrigo':
    print('Que nome bonito.')
elif nome == 'Maria' or nome == 'Joao' or nome == 'Jose':
    print('Seu nome é normal no Brasil.')
elif nome in ('Marcos Japones ELio'):
    print('Otimo nome pra se ter')
else:
    print('Seu nome é normal')
print('Tenha um bom dia {}'.format(nome))