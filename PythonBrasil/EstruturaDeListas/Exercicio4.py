#Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.

letras = []
consoantes = []
for i in range(10):
    letra = str(input('Entre com uma letra: '))
    letras.append(letra[0])
#lista.sort(reverse=True)
#print(len(letras))

for y in letras:
    if y in 'aeiou':
        consoantes.append(y)

print(f'Consoantes: {consoantes}')