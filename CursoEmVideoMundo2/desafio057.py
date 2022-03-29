resultado = False
while resultado != True:
    sexo = str(input('Entrecom o sexo [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        resultado = True
    else:
        print('Opção inválida.')
        resultado = False
print('O Sexo selecionado foi {}.'.format(sexo))
