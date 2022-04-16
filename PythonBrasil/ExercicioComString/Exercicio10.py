# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número
# até 99 e imprima-o na tela por extenso.

numeros = {
    0: 'zero',
    1: 'um',
    2: 'dois',
    3: 'tres',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quize',
    16: 'dezesseis',
    17: 'dezesete',
    18: 'dezoito',
    19: 'dezenove',
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta',
    60: 'sessenta',
    70: 'setenta',
    80: 'oitenta',
    90: 'noventa'
}
numero_string = ''
numero_formatado = ''
unidade = 0
dezena = 0
while True:
    numero = int(input('Entre com um numero 0 - 99: '))
    if numero > 99:
        print('Informe um numero entre 0 e 99.')
        continue
    elif numero_string[0:1] == '0':
        numero_formatado = 'zero'
    elif numero >= 20:
        numero_string = str(numero)
        if numero_string[1:2] != '0':
            dezena = int(f'{str(numero)[0:1]}0')
            unidade = int(f'{str(numero)[1:2]}')
            numero_formatado = f'{numeros[dezena]} e {numeros[unidade]}'
        else:
            numero_formatado = numeros[numero]
    else:
        numero_formatado = numeros[numero]
    break
print(numero_formatado)