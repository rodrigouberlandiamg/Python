# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('Entre com uma letra: '))
if letra[0] in 'qwertyuiopasdfghjklçzxcvbnm':
    if letra[0] in 'aeiou':
        print(f'A letra {letra[0]} e vogal.')
    else:
        print(f'A letra {letra[0]} e consoante.')
else:
    print(f'Erro o caracter {letra[0]} não pertence a classe das vogais e consoantes.')