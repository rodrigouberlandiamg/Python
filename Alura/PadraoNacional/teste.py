
from validate_docbr import CPF
class ValidaCpf:
    def __init__(self, documento):
        self.analisa_cpf(documento)

    def analisa_cpf(self, documento):
        if len(documento) == 11:
            valida_cpf = CPF()
            if valida_cpf.validate(documento):
                self.cpf = documento
                print('CPF salvo')
            else:
                print('CPF inserido não é valido')
        else:
            print('Número de digitos incorreto')

cpf_um = 1235436791
cpf_dois = 12354367912
cpf_tres = '12354367996'

objeto_cpf_um = ValidaCpf(cpf_um )
objeto_cpf_dois = ValidaCpf(cpf_dois )
objeto_cpf_tres = ValidaCpf(cpf_tres )