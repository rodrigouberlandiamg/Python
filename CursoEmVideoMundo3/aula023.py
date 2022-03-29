'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'Ocorreu um erro inesperado: {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte sempre.')'''
######################################################
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Ocorreu um erro de tipos de valores.')
except ZeroDivisionError:
    print('Não é possível dividir o numero por zero.')
except KeyboardInterrupt:
    print('O usuario prefere nao informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte sempre.')