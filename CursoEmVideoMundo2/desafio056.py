soma_idade = 0
idade_p = 0
mulher_menor_20 = 0
for c in range(0,4):
    nome = str(input('Entre com o nome: ')).upper()
    idade = int(input('Entre com a idade: '))
    sexo = str(input('Entre com o sexo "M" ou "F": ')).upper()
    soma_idade = soma_idade + idade
    if idade >= idade_p and sexo == 'M':
        idade_p = idade
        nome_velho = nome
    if idade < 20 and sexo == 'F':
        mulher_menor_20 = mulher_menor_20 + 1
media = soma_idade/4
print('O homem mais velho é {} com idade de {}'.format(nome_velho,idade_p))
print('Existem {} mulher(es) com menos de 20 anos de idade.'.format(mulher_menor_20))