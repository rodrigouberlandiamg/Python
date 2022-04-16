# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = float(input('Entre com a nota do aluno 0-10: '))
    if nota < 10 and nota > 0:
        print(f'Nota digitada {nota}.')
        break
    else:
        print(f'A nota {nota} digitada esta inválida tem que estar entre 0 e 10.')