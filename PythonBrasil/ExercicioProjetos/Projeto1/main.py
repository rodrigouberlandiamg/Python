from calculo_class import calculo
from arquivo_class import arquivo
arq = arquivo()
dados = calculo()
# print(dados.media_total())
# print(dados.espaco_total())
# print(dados.media_usuario(float(dados.espaco_total())))
# print(dados)
arq.criar_relatorio(dados.media_usuario(dados.espaco_total()),dados.espaco_total(),dados.media_total())

