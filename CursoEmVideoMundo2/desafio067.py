while True:
    n = int(input('Qual Tabuada deseja visualizar: '))
    if n < 0:
        break
    print(f'Tabua de [{n}] ')
    for c in range(0,11):
        m = n * c
        print(f'{n} x {c} = {m}')
print('FIM')
