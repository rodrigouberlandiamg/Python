# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_a = []
vetor_b = []
vetor_c = []
vetor_abc = []

print(f'Vetor A')
for x in range(10):
    numero = float(input(f'Entre com o numero posicao [{x}]: '))
    vetor_a.append(numero)

print(f'Vetor B')
for x in range(10):
    numero = float(input(f'Entre com o numero posicao [{x}]: '))
    vetor_b.append(numero)

print(f'Vetor C')
for x in range(10):
    numero = float(input(f'Entre com o numero posicao [{x}]: '))
    vetor_c.append(numero)

for x in range(10):
    vetor_abc.append(vetor_a[x])
    vetor_abc.append(vetor_b[x])
    vetor_abc.append(vetor_c[x])

print(vetor_abc)