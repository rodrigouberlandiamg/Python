from random import shuffle
a1 = str(input('Entre com o nome do primeiro aluno: '))
a2 = str(input('Entre com o nome do segundo aluno: '))
a3 = str(input('Entre com o nome do terceiro aluno: '))
a4 = str(input('Entre com o nome do quarto aluno: '))
alunos = [a1,a2,a3,a4]
shuffle(alunos)
print('A ordem de apresentação é o {}'.format(alunos))
