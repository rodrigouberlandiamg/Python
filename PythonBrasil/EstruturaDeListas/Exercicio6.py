# Faça um Programa que peça as quatro notas de 10 alunos, calcule e
# armazene num vetor a média de cada aluno, imprima o número de alunos
# com média maior ou igual a 7.0

alunos = {}

for i in range(2):
    notas = []
    soma_notas = 0
    media_notas = 0
    for y in range(4):
        nota = float(input(f'Entre com a nota [{i}]: '))
        notas.append(nota)
        soma_notas += nota
    media_notas = soma_notas/len(notas)
    #alunos[i] = notas
    alunos[i] = media_notas

count = 0
for x in alunos:
    if alunos[x] >= 7:
        count += 1

print(f'Existem {count} alunos com média maior que 7.0.')