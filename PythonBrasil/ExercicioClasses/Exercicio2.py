# Classe Quadrado: Crie uma classe que modele um quadrado:
#
#     Atributos: Tamanho do lado
#     Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self,tamanho_lado):
        self.__tamanho_lado = tamanho_lado

    @property
    def tamanho_lado(self):
        return self.__tamanho_lado

    @tamanho_lado.setter
    def tamanho_lado(self,tamanho_lado):
        self.__tamanho_lado = tamanho_lado

    def mudar_valor_lado(self,novo_valor):
        self.tamanho_lado = novo_valor

    def retorna_valor_lado(self):
        return self.tamanho_lado

    def calcula_area(self):
        return self.tamanho_lado ** 2

quadrado = Quadrado(5)
quadrado.mudar_valor_lado(3)
print(f'O tamanho do lado do quadrado é de {quadrado.retorna_valor_lado()}')
print(f'O Valor da área do quadrado é de {quadrado.calcula_area()}')
