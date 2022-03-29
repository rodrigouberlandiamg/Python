cedula1 = cedula10 = cedula20 = cedula50 = 0
valorsac = float(input('Qual valor deseja sacar: '))
if valorsac >= 50:
    while valorsac >= 50:
        cedula50 += 1
        valorsac = valorsac - 50
    if cedula50 != 0:
        print(f'Saque de {cedula50} cedulas de R$50,00')
    while valorsac >= 20 < 50:
        cedula20 += 1
        valorsac = valorsac - 20
    if cedula20 != 0:
        print(f'Saque de {cedula20} cedulas de R$20,00')
    while valorsac >= 10 < 20:
        cedula10 += 1
        valorsac = valorsac -10
    if cedula10 != 0:
        print(f'Saque de {cedula10} cedulas de R$10,00')
    while valorsac >= 1 < 9:
        cedula1 += 1
        valorsac = valorsac - 1
    if cedula1 != 0:
        print(f'Saque de {cedula1} cedulas de R$1,00')
print('FIM')