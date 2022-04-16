# Classe Bola: Crie uma classe que modele uma bola:
#
#     Atributos: Cor, circunferência, material
#     Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self,cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    @property
    def cor(self):
        return self.__cor

    @property
    def circunferencia(self):
        return self.__circunferencia

    @property
    def material(self):
        return self.__material

    @cor.setter
    def cor(self,cor):
        self.__cor = cor

    @circunferencia.setter
    def circunferencia(self, circunferencia):
        self.__circunferencia = circunferencia

    @material.setter
    def material(self, material):
        self.__material = material

    def trocaCor(self,nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(f'Cor: {self.__cor}')

    def __str__(self):
        return f'Cor: {self.cor}, Circunferencia: {self.circunferencia} e material é {self.material}'

nova_bola = Bola('Azul','Redonda','Couro')
nova_bola.mostraCor()
nova_bola.trocaCor('Verde')
nova_bola.mostraCor()
print(nova_bola)