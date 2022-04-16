# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de
# centenas, dezenas e unidades do mesmo.
#
#     Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#     326 = 3 centenas, 2 dezenas e 6 unidades
#     12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20,
#     10, 21, 11, 1, 7 e 16

while True:
    numero = input('Entre com um nomero de 0-1000: ')
    #print(len(numero))
    #print(numero[0])
    if numero.isnumeric():
        #print('é numero.')
        if int(numero) >= 0 and int(numero) <= 1000:
            if len(numero) == 1:
                print(f'{numero[0]} unidade(s).')
            elif len(numero) == 2:
                print(f'{numero[0]} dezena(s) e {numero[1]} unidade(s).')
            elif len(numero) == 3:
                print(f'{numero[0]} centena(s) {numero[1]} dezena(s) e {numero[2]} unidade(s).')
            elif len(numero) == 4:
                print(f'{numero[0]} milhar {numero[1]} centana {numero[2]} dezena e {numero[3]} unidade.')
            break
        else:
            print(f'Entre com um numero entre 0-1000 o valor {numero} informado esta fora do range.')
    else:
        print(f'Digite numero conforme solicitação.')