import pandas as pd
from collections import Counter

class Lotofacil:
    def __init__(self):
        pass

    def limpa_arquivo(self,arquivo_original,arquivo_novo):
        with open(arquivo_original,'r') as file:
            for linha in file:
                if not linha[0] == ';':
                    with open(arquivo_novo,'a') as file_dest:
                        file_dest.write(linha)

    def analisa_frequencia_de_numeros(self,arquivo,data_ini,data_fim):
        dados_originais = pd.read_csv(arquivo,sep=';',encoding='latin1')
        dados_originais['Data_Sorteio'] = pd.to_datetime(dados_originais['Data_Sorteio'])
        # print(dados_originais.info())
        dados_necessarios_com_data = dados_originais[['Data_Sorteio','Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9','Bola10','Bola11','Bola12','Bola13','Bola14','Bola15']]
        dados_filtrados = dados_necessarios_com_data.query(f"Data_Sorteio >= '{data_ini}' and Data_Sorteio <= '{data_fim}'")
        # print(dados_filtrados)
        dados_necessarios = dados_filtrados[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10','Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']]
        # print(dados_necessarios)
        dados_necessarios_lists = dados_necessarios.values.tolist()
        lista_total = []
        total_jogos = 0
        for lista in dados_necessarios_lists:
            # print(lista)
            total_jogos += 1
            for item in lista:
                lista_total.append(item)
        # print(lista_total)
        lista_count = Counter(lista_total)
        # print(type(lista_count))
        # print(lista_count)
        proporcoes = [(bola,qtdeaparece) for bola,qtdeaparece in lista_count.items()]
        proporcoes = Counter(dict(proporcoes))
        mais_comuns = proporcoes.most_common(15)
        print(f'Proporções: {proporcoes}')
        lista_jogos = []
        for bola, proporcao in mais_comuns:
            lista_jogos.append(bola)
            # print(bola,end=' - ')
        lista_jogos.sort()
        print(f'Jogo: {lista_jogos}')
        print(f'Total de Jogos: {total_jogos}')

if __name__ == '__main__':
    lotofacil = Lotofacil()
    # lotofacil.limpa_arquivo('lotofacil_resultados.csv','lotofacil_resultados_filtrado.csv')
    # for i in range(12):
    #     lotofacil.analisa_frequencia_de_numeros('lotofacil_resultados_filtrado.csv',f'2021-{str(i+1).zfill(2)}-01','2022-04-06')
    lotofacil.analisa_frequencia_de_numeros('lotofacil_resultados_filtrado.csv', '2022-01-10','2022-04-10')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
