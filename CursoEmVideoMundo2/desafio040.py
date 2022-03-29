n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERACAO')
elif media >= 7:
    print('APROVADO')