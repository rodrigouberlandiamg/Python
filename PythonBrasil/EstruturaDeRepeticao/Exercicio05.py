# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
# iniciais. Valide a entrada e permita repetir a operação.
while True:
    pais_a = int(input('Entre com o numero de habitantes do pais A: '))
    pais_b = int(input('Entre com o numero de habitantes do pais B: '))
    crescimento_a = float(input('Entre com o percentual de cresciemnto da população do pais A: '))
    crescimento_b = float(input('Entre com o percentual de cresciemnto da população do pais B: '))
    anos = 0
    while True:
        pais_a = pais_a + (pais_a*(crescimento_a/100))
        pais_b = pais_b + (pais_b * (crescimento_b / 100))
        if pais_a <= pais_b:
            anos += 1
        else:
            break
    print(f'São necessários {anos} anos para que a população do pais A seja maior ou igual a população do pais B.')
    while True:
        sair = input('Deseja outra consulta S/N: ')
        if sair[0].upper() in ('SN'):
            break
    if sair.upper() == 'N':
        print('Fechando aplicação. Finalizado.')
        break
