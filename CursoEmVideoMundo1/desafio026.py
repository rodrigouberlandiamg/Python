frase = str(input('Entre com uma frase: ')).strip()
print('A letra A aparece {} vezes. Primeira vez posição: {} e ultima vez posição: {}'.format(frase.lower().count('a',0,len(frase)),frase.find('a')+1,frase.rfind('a')+1))
