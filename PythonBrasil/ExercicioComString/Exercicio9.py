# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF
# no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos
# dígitos verificadores e dos caracteres de formatação.

cpf = str(input(f'Entre com o CPF: '))
primeiros_digitos = cpf[:9]
soma = 0
count_pos = 0
tamanho_primeiros_digitos = len(primeiros_digitos)-1
#print(primeiros_digitos)
#print(cpf)
for x in range(2,10):
    soma += x*(int(primeiros_digitos[tamanho_primeiros_digitos-count_pos]))
    count_pos += 1
primeiro_digito = 0
resto = soma % 11
if resto < 2:
    primeiro_digito = 0
elif resto >= 2:
    primeiro_digito = 11 - resto
#print(primeiro_digito)

soma = 0
count_pos = 0
primeiros_digitos = f'{primeiros_digitos}{primeiro_digito}'
tamanho_primeiros_digitos = len(primeiros_digitos)-1
for x in range(2,11):
    soma += x*(int(primeiros_digitos[tamanho_primeiros_digitos-count_pos]))
    count_pos += 1
segundo_digito = 0
resto = soma % 11
if resto < 2:
    segundo_digito = 0
elif resto >= 2:
    segundo_digito = 11 - resto
#print(segundo_digito)
primeiros_digitos = f'{primeiros_digitos}{segundo_digito}'
#print(f'CPF Validado: {primeiros_digitos}')

if cpf == f'{primeiros_digitos}':
    print('CPF OK')
else:
    print(f'CPF Invalido. O certo seria: {primeiros_digitos}')

