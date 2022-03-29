print('\033[0;30;41mOla mundo.\033[m')
print('\033[4;33;44mOla mundo.\033[m')
print('\033[1;35;43mOla mundo.\033[m')
print('\033[30;42mOla mundo.\033[m')
print('\033[mOla mundo.\033[m')
print('\033[7;30mOla mundo.\033[m')
print('Ola mundo.\033[m')

nome = 'rodrigo'
print('Ola, {}{}{} !!!'.format('\033[4;34m',nome,'\033[m'))

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m','pretobranco':'\033[7;30m'}
print('Ola prazer {}{}{}'.format(cores['pretobranco'],nome, cores['limpa']))
