continuar = valida = cadastro = True
maior18 = homens = mulhermenor20 = 0
i = o = s = ''
while continuar == True:
    valida = cadastro = True
    i = int(input('Entre com a Idade: '))
    while valida == True:
        s = str(input('Selecione sexo [M/F]: ')).upper()
        if s[0] == 'M':
            valida = False
        elif s[0] == 'F':
            valida = False
        else:
            valida = True
    if i > 18:
        maior18 += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        mulhermenor20 += 1
    while cadastro == True:
        o = str(input('Deseja outro cadastro [S/N]: ')).upper()
        print(o[0])
        if o[0] == 'S':
            cadastro = False
        elif o[0] == 'N':
            cadastro = False
            print('Sair')
        else:
            cadastro = True
    if o[0] == 'N':
        break
print(f'Existem {maior18} pessoa(s) maior de 18 anos.')
print(f'Existem {homens} homem(ns) cadastrado(s).')
print(f'Existem {mulhermenor20} melher menor de 20 anos.')
print('FIM')