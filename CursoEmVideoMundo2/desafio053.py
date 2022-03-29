print('VERIFICADOR DE PALINDROMO')
frase = str(input('Escreva uma frase: ')).strip()
tamanho_frase = len(frase)-1
nova_frase = ''
for c in range(tamanho_frase,-1,-1):
    nova_frase = nova_frase + frase[c]
if nova_frase.lower() == frase.lower():
    print('Esta frase "{}" é POLINDROMO'.format(frase))
else:
    print(('Esta frase "{}" NAO E PROLINDROMO.'.format(frase)))