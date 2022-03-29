import random
a1 = str(input('Entre com o nome do primeiro aluno: '))
a2 = str(input('Entre com o nome do segundo aluno: '))
a3 = str(input('Entre com o nome do terceiro aluno: '))
a4 = str(input('Entre com o nome do quarto aluno: '))
alunos = [a1,a2,a3,a4]
print('O aluno sorteado para apagar o quadro é o {}'.format(random.choice(alunos)))
