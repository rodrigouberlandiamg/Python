# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
# verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

qtde_pessoas = int(input('Entre com a quantidade de pessoas: '))
idade = 0
media = 0
for i in range(1,qtde_pessoas+1):
    idade = int(input(f'Entre com a idade da pessoa [{i}]: '))
    media += idade
media = media/qtde_pessoas
print(f'A média de idade dessa turma é de {media}.')
if media >= 0 and media <= 25:
    print(f'Esta turma é de idade JOVEM.')
elif media >= 6 and media <= 60:
    print(f'Esta turma é de idade ADULTA.')
else:
    print(f'Esta turma é de idade IDOSA.')