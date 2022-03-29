nome = str(input('Entre com o nome completo: ')).strip()
listanome = nome.split()
#print(len(listanome))
print('O primeiro nome é {} e o ultimo nome é {}'.format(listanome[0],listanome[len(listanome)-1]))

