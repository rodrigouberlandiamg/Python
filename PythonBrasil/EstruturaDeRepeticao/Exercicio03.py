# Faça um programa que leia e valide as seguintes informações:
#
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input('Entre com o nome: ')
    idade = int(input('Entre com a idade: '))
    salario = float(input('Entre com o salario: R$'))
    sexo = input('Entre com o sexo M/F: ').upper()
    estadoCivil = input('Entre com o estado civil (s,c,v,d): ')
    erro = 0

    if len(nome) < 3:
        print('Informe o nome com mais de 3 caracteres.')
        erro += 1
    if idade < 0 and idade > 150:
        print('Informa a idade entre 0 e 150.')
        erro += 1
    if salario < 0:
        print('Entre com o salario maior de R$0,00.')
        erro += 1
    if sexo[0] not in ('MF'):
        print('Entre com o sexo M/F.')
        erro += 1
    if estadoCivil[0].upper() not in ('SCVD'):
        print('Entre com o estado civil (s,c,v,d).')
        erro += 1
    if erro != 0:
        print(f'Foram encontrados todal de {erro} erro(s). Favor informar os dados corretamente.')
    else:
        print(f'Dados cadastrados nome {nome.upper()} com idade de {idade} ganhando salário de R${salario} do sexo {sexo.upper()} e estado civil {estadoCivil.upper()}.')
        break
