# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário
# (incluindo espaços em branco), conte:
#
#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.

count_espaco = 0
count_vogais = 0
frase = str(input('Entre com uma frase: '))
for x in frase:
    if x in 'aeiou':
        count_vogais += 1
    if x in ' ':
        count_espaco += 1

print(f'Exite(m) {count_vogais} vogais na frase {frase}')
print(f'Exite(m) {count_espaco} espaços na frase {frase}')