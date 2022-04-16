# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento
# e são iguais ou diferentes no conteúdo.
#
#     Compara duas strings
#     String 1: Brasil Hexa 2006
#     String 2: Brasil! Hexa 2006!
#     Tamanho de "Brasil Hexa 2006": 16 caracteres
#     Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#     As duas strings são de tamanhos diferentes.
#     As duas strings possuem conteúdo diferente.

string1 = str(input('Entre com a string1: '))
string2 = str(input('Entre com a string2: '))

t_str1 = len(string1)
t_str2 = len(string2)

print(f'String 1: {string1}')
print(f'String 2: {string2}')
print(f'Tamanho de {string1}: {len(string1)}')
print(f'Tamanho de {string2}: {len(string2)}')
if t_str1 == t_str2:
    print('As duas strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')
if string1.upper() == string2.upper():
    print('As duas string tem o mesmo conteudo.')
else:
    print('As duas string possuem conteudo diferente.')