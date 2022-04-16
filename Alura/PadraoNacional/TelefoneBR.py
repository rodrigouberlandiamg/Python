import re
class TelefoneBR:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Numero incorreto !!!')

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self,telefone):
        padrao_telefone = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta_telefone = re.findall(padrao_telefone, telefone)
        if resposta_telefone:
            return True
        else:
            return False

    def format_numero(self):
        padrao_telefone = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        reposta = re.search(padrao_telefone,self.numero)
        numero_formatado = f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
        return numero_formatado



telefone = '5534997531954'
telefone_objeto = TelefoneBR(telefone)
padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
resposta = re.search(padrao,telefone)
telefone_objeto.format_numero()
print(telefone_objeto)