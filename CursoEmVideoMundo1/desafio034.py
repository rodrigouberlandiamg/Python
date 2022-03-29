salario = float(input('Entre com o Salario: '))
if salario > 1250.00:
    print('O salario {} teve aumento de 10% e agora é R${:.2f}'.format(salario,float((salario*10/100))+salario))
else:
    print('O salario {} teve aumento de 15% e agora é R${:.2f}'.format(salario, float((salario * 15 / 100))+salario))