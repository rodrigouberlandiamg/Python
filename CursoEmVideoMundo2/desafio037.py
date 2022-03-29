
n = int(input('Entre com um numero inteiro: '))
print('Informar a base de conversão')
print('''1 = BINARIO
         2 = OCTAL
         3 = HEXADECIMAL: ''')
base = str(input('Sua Opção: '))
if base == '1':
    print('Esse numero em BINARIO é {}'.format(bin(n)[2:]))
elif base == '2':
    print('Esse numero em OCTAL é {}'.format(oct(n)[2:]))
elif base == '3':
    print('Esse numero em HEXADECIMAL é {}'.format(hex(n)[2:]))
else:
    print('Opção INVALIDA.')
print('FIM')