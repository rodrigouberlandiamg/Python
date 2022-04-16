# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular
# a média alcançada por aluno e presentar:
#
#     A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#     A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#     A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input('Entre com a primeira nota do aluno: '))
nota2 = float(input('Entre com a segunda nota do aluno: '))
nota3 = float(input('Entre com a terceira nota do aluno: '))
media = (nota1+nota2+nota3)/3
if media >= 7 and media <= 9.9:
    print(f'O aluno com as notas {nota1}, {nota2} e {nota3} foi aprovado com média {media}.')
elif media < 7:
    print(f'O aluno com as notas {nota1}, {nota2} e {nota3} foi reprovado com média {media}.')
elif media == 10:
    print('Aprovado com Distinção.')