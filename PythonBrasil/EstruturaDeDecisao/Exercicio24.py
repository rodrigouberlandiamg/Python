# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja
# realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#
#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.
while True:
    try:
        print('===========================')
        print('1 - Par ou Impar')
        print('2 - Positivo ou negativo')
        print('3 - Inteiro ou decimal')
        print('4 - Sair')
        print('===========================')
        op = input('Qual opção: ')
        if op in ('1','2','3','4'):
            if op != '4':
                n1 = float(input('Entre com o primeiro numero: '))
                n2 = float(input('Entre com o segundo numero: '))
            if op == '1':
                if n1 % 2 == 0:
                    print(f'O numero {n1} é PAR.')
                else:
                    print(f'O numero {n1} é IMPAR.')
                if op == '1':
                    if n2 % 2 == 0:
                        print(f'O numero {n2} é PAR.')
                    else:
                        print(f'O numero {n2} é IMPAR.')
            elif op == '2':
                if n1 > 0:
                    print(f'O numero {n1} é positivo.')
                elif n1 < 0:
                    print(f'O numero {n1} é negativo.')
                elif n1 == 0:
                    print(f'O numero {n1} é nulo.')
                if n2 > 0:
                    print(f'O numero {n2} é positivo.')
                elif n2 < 0:
                    print(f'O numero {n2} é negativo.')
                elif n2 == 0:
                    print(f'O numero {n2} é nulo.')
            elif op == '3':
                if round(float(n1)) == float(n1):
                    print(f'Este numero {n1} é inteiro.')
                else:
                    print(f'Este numero {n1} não é inteiro.')
                if round(float(n2)) == float(n2):
                    print(f'Este numero {n2} é inteiro.')
                else:
                    print(f'Este numero {n2} não é inteiro.')
            elif op == '4':
                print('FIM')
                break
        else:
            print('Escolha uma opção válida.')
    except Exception as e:
        print(f'Entre com o valor numerico valido. Erro: {e.args}')