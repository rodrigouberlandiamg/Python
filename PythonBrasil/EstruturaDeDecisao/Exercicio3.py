# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Entre com o sexo [M/F]: '))
if sexo in "MmFf":
    if sexo in "mM":
        print('Sexo MASCULINO')
    else:
        print('Sexo FEMININO.')
else:
    print('Sexo inválido.')