# Faça um programa que leia 5 números e informe a soma e a média dos números.
numero = 0
soma = 0
for x in range (0,5):
    numero = float(input(f'Entre com o numero [{x}]: '))
    soma += numero
print(f'A soma dos numeros digitados é igual a {soma} e sua média é {soma/(x+1)}.')