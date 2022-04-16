# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
# atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
# O programa deve ser encerrado quando não for informado o nome do atleta. A saída do
# programa deve ser conforme o exemplo abaixo:
#
# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

atletas = {}
saltos = []
indice = 0
dic_saltos = {
    0 : 'Primeiro',
    1 : 'Segundo',
    2 : 'Terceiro',
    3 : 'Quarto',
    4 : 'Quinto'
}
while True:
    atleta = str(input(f'Entre com o nome do atleta: '))
    if atleta == '':
        break
    else:
        atletas[f'nome_{indice}'] = atleta
        for x in range(5):
            salto = float(input(f'Salto [{x}]: '))
            saltos.append(salto)
        copia_saltos = saltos.copy()
        saltos.clear()
        atletas[f'saltos_{indice}'] = copia_saltos
    indice += 1

#print(atletas)

for x in atletas:
    if 'nome' in x:
        print(f'Atleta: {atletas[x]}\n')
    if 'saltos' in x:
        icount = 0
        for s in atletas[x]:
            print(f'{dic_saltos[icount]} salto: {s} m')
            icount += 1
        print('')

print(f'Resultado Final:')

for x in atletas:
    if 'nome' in x:
        print(f'Atleta: {atletas[x]}')
    if 'saltos' in x:
        icount = 0
        soma = 0
        print(f'Saltos',end=': ')
        for s in atletas[x]:
            print(f'{atletas[x][icount]}',end=' - ')
            soma += atletas[x][icount]
            icount += 1
        print('')
        print(f'Média dos saltos: {soma/len(atletas[x])}')
        print('')
print('FIM')
