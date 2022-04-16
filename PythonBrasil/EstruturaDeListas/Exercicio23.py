# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco
# no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede
# precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior
# espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte
# arquivo, chamado "usuarios.txt":
#
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
#
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar
# um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
#
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso
#
# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%
#
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória,
# caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço
# ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada,
# que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser
# feito através de uma função, que será chamada pelo programa principal.

def grava_file_log(mensagem):
    print(mensagem)
    with open('c:/temp/relatorio.txt','a+') as file_log:
        file_log.write(f'{mensagem}\n')

usuarios = {}

with open('c:/temp/usuarios.txt','r') as file_user:
    count = 0
    soma_total = 0
    soma_tot_user = 0
    for x in file_user:
        usuarios[f'usuario_{count}'] = x[:15].replace(' ','')
        usuarios[f'disco_{count}'] = x[16:].replace('\n','')
        soma_total += int(usuarios[f'disco_{count}'])
        soma_tot_user += 1
        count += 1
media_user = soma_total/soma_tot_user
#print(usuarios)

for x in usuarios:
    if 'usuario' in x:
        grava_file_log(f'{usuarios[x]}                 ')
    if 'disco' in x:
        grava_file_log(f'{usuarios[x]}                 ')
        grava_file_log(f'{(100 * int(usuarios[x])) / soma_total:.2f}')

grava_file_log(f'Espaço total ocupado: {soma_total:.2f} MB')
grava_file_log(f'Espaço médio ocupado: {media_user:.2f} MB')
