# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
#
#     O arquivo de entrada possui o seguinte formato:
#
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
#
#     O arquivo de saída possui o seguinte formato:
#
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
#
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True
arquivo_verificar = open('arq_ip.txt','r')
arquivo_ips_corretos = open('arq_ip_correto.txt','a')
arquivo_ips_incorretos = open('arq_ip_incorreto.txt','a')
arquivo_ips_incorretos.write('IPS INCORRETOS\n')
arquivo_ips_corretos.write('IPS CORRETOS\n')
for linha in arquivo_verificar:
    if validIP(linha):
        arquivo_ips_corretos.write(linha)
    else:
        arquivo_ips_incorretos.write(linha)



#Fechando arquivos
arquivo_ips_incorretos.close()
arquivo_verificar.close()
arquivo_ips_corretos.close()

