# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
# isósceles ou escaleno.
#
#     Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#     Triângulo Equilátero: três lados iguais;
#     Triângulo Isósceles: quaisquer dois lados iguais;
#     Triângulo Escaleno: três lados diferentes;

ladoa = float(input('Entre com o valor do lado A de um triângulo: '))
ladob = float(input('Entre com o valor do lado B de um triângulo: '))
ladoc = float(input('Entre com o valor do lado C de um triângulo: '))
if ladoa+ladob > ladoc:
    if ladoa == ladob == ladoc:
        print('Triangulo Equilatero.')
    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print('Triangulo Isosceles')
    elif ladoa != ladob != ladoc:
        print('Triangulo Escaleno')
else:
    print('Não forma Triangulo.')