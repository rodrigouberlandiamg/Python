# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
# crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país
# A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
pais_a = 80000
pais_b = 200000
crescimento_a = 3
crescimento_b = 1.5
anos = 0
while True:
    pais_a = pais_a + (pais_a*(crescimento_a/100))
    pais_b = pais_b + (pais_b * (crescimento_b / 100))
    if pais_a <= pais_b:
        anos += 1
    else:
        break
print(f'São necessários {anos} anos para que a população do pais A seja maior ou igual a população do pais B.')