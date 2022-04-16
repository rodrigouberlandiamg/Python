# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    usuario = input('Entre com o nome do usuario: ')
    senha = input(f'Entre com a senha para o usuario {usuario}: ')
    if usuario != senha:
        print(f'Usuario {usuario} cadastrado com sucesso.')
        break
    else:
        print('Usuario e senha iguais favor informar senha diferente do nome do usuario.')