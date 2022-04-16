# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
# número elevado ao segundo número. Não utilize a função de potência da linguagem.
num1 = int(input('Entre com um numero base: '))
num2 = int(input('Entre com outro numero expoente: '))
soma = 1
#print(f'{num1**num2}')
for x in range(0,num2):
    soma = soma * num1
    #print(f'{soma}')
print(f'Potencia: {soma}')