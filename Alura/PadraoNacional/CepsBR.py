import requests


class BuscaEndereco:
    def __init__(self,cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('Cep inválido.')


    def valida_cep(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        return r.json()['bairro'],r.json()['localidade'],r.json()['uf']


cep = 38411201
validador_cep = BuscaEndereco(cep)
print(validador_cep.format_cep())
print(validador_cep.acessa_via_cep())
