op = 0
while op != 5:
    n1 = int(input('Entre com um valor: '))
    n2 = int(input('Entre com outro valor: '))
    print('='*30)
    print('Selecione uma opção')
    print('[1] - SOMA')
    print('[2] - MULTIPLICACAO')
    print('[3] - MAIOR')
    print('[4] - NOVO NUMERO')
    print('[5] - SAIR')
    print('='*30)
    op = int(input('OPCAO: '))
    if op == 1:
        calculo = n1+n2
        print('A soma é {}'.format(calculo))
    elif op == 2:
        calculo = n1*n2
        print('A multiplicação é  {}'.format(calculo))
    elif op == 3:
        if n1 == n2:
            print('Os numeros são iguais')
        if n1 > n2:
            print('O maior numero é o {}'.format(n1))
        elif n2 > n1:
            print('O maior numero é o {}'.format(n2))
    elif op == 4:
        print('NOVA PROCESSO.')
    elif op == 5:
        print('SAINDO DO SISTEMA.')
    else:
        print('Opção invalida.')
print('FIM')