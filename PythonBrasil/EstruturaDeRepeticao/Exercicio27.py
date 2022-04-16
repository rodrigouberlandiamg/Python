# Faça um programa que calcule o número médio de alunos por turma. Para isto,
# peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas
# não podem ter mais de 40 alunos.

turmas = int(input('Entre com a quantidade de turmas: '))
alunos = 0
media = 0
for i in range(1,turmas+1):
    while True:
        alunos = int(input(f'Entre com a quantidade de alunos para a turma [{i}]: '))
        if alunos <= 40:
            media += alunos
            break
        else:
            print('A quantidade de alunos por turma tem q ser inferior menos ou igual a 40.')
print(f'A quantidade de alunos média por turma é de {media/turmas}.')

