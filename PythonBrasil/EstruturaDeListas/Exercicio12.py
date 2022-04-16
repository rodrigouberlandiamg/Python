# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

alunos = []
dado_aluno = {}
tamanho_loop = 2
altura_media = 0
soma_alturas = 0
for x in range(tamanho_loop):
    dado_aluno['cod'] = x
    dado_aluno['idade'] = int(input(f'Entre com a idade do aluno [{x}]: '))
    dado_aluno['altura'] = float(input(f'Entre com a altura do aluno [{x}]: '))
    soma_alturas += dado_aluno['altura']
    copia_dados = dado_aluno.copy()
    alunos.append(copia_dados)
altura_media = soma_alturas/tamanho_loop
count = 0
for x in range(tamanho_loop):
    if alunos[x]['idade'] > 13 and alunos[x]['altura'] < altura_media:
        count += 1
print(f'Existe(m) {count} aluno(s) com idade superior a 13 anos e abaixo da altura media de {altura_media}.')