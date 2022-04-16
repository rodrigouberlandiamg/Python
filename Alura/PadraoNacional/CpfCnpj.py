from validate_docbr import CPF,CNPJ

class Documento:

    # factory
    """
    Para conseguirmos usar qualquer instância retornada pelo Factory livremente, os métodos das classes filhas
    precisam ser iguais.
    """
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError('Quantida de Dígitos esta incorreta.')

class DocCPF():
    def __init__(self,documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('Cpf inválido.')

    def __str__(self):
        return self.format()

    def valida(self,documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCNPJ():
    def __init__(self,documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('Cnpj inválido.')

    def __str__(self):
        return self.format()

    def valida(self,documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)



# class CpfCnpj():
#     def __init__(self,documento,tipo):
#         self.tipo = tipo
#         if self.tipo.lower() == 'cpf':
#             if self.cpf_valido(documento):
#                 self.cpf = documento
#             else:
#                 raise ValueError('CPF inválido.')
#         elif self.tipo.lower() == 'cnpj':
#             if self.cnpj_valido(documento):
#                 self.cnpj = documento
#             else:
#                 raise ValueError('CNPJ inválido.')
#         else:
#             raise ValueError('Tipo de documento inválido.')
#
#     def __str__(self):
#         if self.tipo == 'cpf':
#             return self.format_cpf()
#         elif self.tipo == 'cnpj':
#             return self.format_cnpj()
#         else:
#             raise ValueError('Não foi definido o tipo.')
#
#     def cpf_valido(self,cpf):
#         cpf = str(cpf)
#         if len(cpf) == 11:
#             validador_cpf = CPF()
#             return validador_cpf.validate(cpf)
#         else:
#             raise ValueError('Quantidade de dígitos inválido.')
#
#
#     def format_cpf(self):
#         # fatia_um = self.cpf[:3]
#         # fatia_dois = self.cpf[3:6]
#         # fatia_tres = self.cpf[6:9]
#         # fatia_quatro = self.cpf[9:]
#         # return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'
#         mascara_cpf = CPF()
#         return mascara_cpf.mask(self.cpf)
#
#     def cnpj_valido(self,cnpj):
#         cnpj = str(cnpj)
#         if len(cnpj) == 14:
#             validador_cpf = CNPJ()
#             return validador_cpf.validate(cnpj)
#         else:
#             raise ValueError('Quantidade de dígitos inválido.')
#
#     def format_cnpj(self):
#         mascara_cnpj = CNPJ()
#         return mascara_cnpj.mask(self.cnpj)