from CpfCnpj import Documento


# cpf_ori = '04279264678'
# objeto_cpf = CpfCnpj(cpf_ori,'cpf')
# print(objeto_cpf.format_cpf())
# print(objeto_cpf)
#
# cnpj_ori = '35379838000112'
# objeto_cnpj = CpfCnpj(cnpj_ori,'cnpj')
# print(objeto_cnpj.format_cnpj())
# print(objeto_cnpj)


# cpf = '04279264678'
# tamanho_cpf = len(cpf)
# print(tamanho_cpf)

exemplo_cnpj = '35379838000112'
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)


exemplo_cpf = '04279264678'
documento = Documento.cria_documento(exemplo_cpf)
print(documento)