#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
soma_nota = 0
for i in range(4):
    nota = float(input(f'Entre com a nota {[i]}: '))
    notas.append(nota)
    soma_nota += nota
media_nota = soma_nota/len(notas)
print(f'A media de notas é: {media_nota}')
