# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de
# um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#
#       Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0        A
#       Entre 7.5 e 9.0         B
#       Entre 6.0 e 7.5         C
#       Entre 4.0 e 6.0         D
#       Entre 4.0 e zero        E
while True:
    nota1 = float(input('Entre com a nota 1: '))
    nota2 = float(input('Entre com a nota 2: '))
    media = (nota1+nota2)/2
    if nota1 > 10 or nota2 > 10:
        print('Entre com valor do nota entre 0 até 10.')
    else:
        break
if media >= 9 and media <= 10:
    conceito = 'A'
elif media >= 7.5 and media < 9:
    conceito = 'B'
elif media >= 6 and media < 7.5:
    conceito = 'C'
elif media >= 4 and media < 6:
    conceito = 'D'
elif media < 4:
    conceito = 'E'
if media >= 6:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'
print(f'Nota 1: {nota1}')
print(f'Nota 2: {nota2}')
print(f'Media: {media}')
print(f'Conceito: {conceito}')
print(f'Situacao: {situacao}')