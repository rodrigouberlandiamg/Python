# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#
#     Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#         tipoCombustivel.
#         valorLitro
#         quantidadeCombustivel
#     Possua no mínimo esses métodos:
#         abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
#         quantidade de litros que foi colocada no veículo
#         abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
#         mostra o valor a ser pago pelo cliente.
#         alterarValor( ) – altera o valor do litro do combustível.
#         alterarCombustivel( ) – altera o tipo do combustível.
#         alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#     OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível
#     total na bomba.

class BombaCombustivel:
    def __init__(self,tipo_combustivel,valor_litro,quantidade_combustivel):
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__quantidade_combustivel = quantidade_combustivel

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @property
    def valor_litro(self):
        return self.__valor_litro

    @property
    def quantidade_combustivel(self):
        return self.__quantidade_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self,tipo_combustivel):
        self.__tipo_combustivel = tipo_combustivel

    @valor_litro.setter
    def valor_litro(self, valor_litro):
        self.__valor_litro = valor_litro

    @quantidade_combustivel.setter
    def quantidade_combustivel(self, quantidade_combustivel):
        self.__quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self,valor):
        self.quantidade_combustivel -= (valor/self.valor_litro)
        return valor/self.valor_litro

    def abastecerPorLitro(self,quantidade):
        self.quantidade_combustivel -= quantidade
        return quantidade*self.valor_litro

    def alterarValor(self,valor):
        self.valor_litro = valor

    def alterarCombustivel(self,tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel

    def alterarQuantidadeCombustivel(self,quantidade):
        self.quantidade_combustivel += quantidade

    def __str__(self):
        return f'Dados da BOMBA\nCombustivel:{self.tipo_combustivel}\nValor Litro: R${self.valor_litro}\nQuantidade Atual: {self.quantidade_combustivel}'

abastecer = BombaCombustivel('Gasolina',6.5,300)
abastecer.abastecerPorValor(100.00)
abastecer.abastecerPorLitro(35)
print(abastecer)
abastecer.alterarCombustivel('Etanol')
abastecer.alterarValor(4.80)
abastecer.alterarQuantidadeCombustivel(300)
abastecer.abastecerPorValor(100.00)
abastecer.abastecerPorLitro(35)
print(abastecer)

