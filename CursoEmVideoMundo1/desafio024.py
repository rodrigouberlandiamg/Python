cidade = str(input('Entre com o nome da cidade: ')).strip()
cidade1 = cidade.split()
print('Existe SANTO: {}'.format('santo' in cidade1[0].lower()))
