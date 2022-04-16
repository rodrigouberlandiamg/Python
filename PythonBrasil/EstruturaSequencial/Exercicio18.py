#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanhoarquivo = float(input('Entre com o tamanho do arquivo em MB: '))
velocidade = float(input('Entre com a velocidade da internet em Mbps: '))
tempo = (tamanhoarquivo)/(velocidade/8)
print(f'O tempo médio de download será de {tempo} minutos.')