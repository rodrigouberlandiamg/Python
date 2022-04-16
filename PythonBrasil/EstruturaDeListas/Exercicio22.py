# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de
# Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área.
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando
# e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#
#     Foi requisitado que você desenvolva um programa para registrar este levantamento.
#     O programa deverá receber um número indeterminado de entradas, cada uma contendo:
#     um número de identificação do mouse o tipo de defeito:
#     necessita da esfera;
#     necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado
#     Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o
#     seguinte relatório:
#
# Quantidade de mouses: 100
#
# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

tipo_defeitos = {
    1:'necessita da esfera',
    2:'necessita de limpeza',
    3:'necessita troca do cabo ou conector',
    4:'quebrado ou inutilizado'
}
registro = {}
index = 0
cod_defeito = 0
relacao_defeito = {}
while True:
    registro[f'indice_{index}'] = index
    cod_defeito = int(input(f'Entre com o código do defeito [{index}]: '))
    if cod_defeito == 0:
        break
    elif cod_defeito < 1 or cod_defeito > 4:
        print('Entre com o código do defeito entre 1 e 4.')
    else:
        registro[f'defeito_{index}'] = cod_defeito
        index += 1

#print(registro)
soma_total = 0
for x in tipo_defeitos:
    #print(x)
    #print(tipo_defeitos[x])
    count_defeito = 0
    for i in registro:
        if 'defeito' in i:
            if x == registro[i]:
                count_defeito += 1
                relacao_defeito[f'quantidade_{tipo_defeitos[x]}'] = count_defeito
                soma_total += 1
                #print(registro[i])
#print(relacao_defeito)

for x in relacao_defeito:
    if 'quantidade' in x:
        print(f'{x}', end='                        ')
        print(f'{relacao_defeito[x]}', end='         ')
        print(f'{(100 * relacao_defeito[x]) / soma_total:.2f}')
