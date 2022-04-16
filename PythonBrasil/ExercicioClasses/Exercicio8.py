# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho
# (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste
# interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos
# diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um
# macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self,nome):
        self.__nome = nome
        self.__bucho = []

    @property
    def nome(self):
        return self.__nome

    @property
    def bucho(self):
        return self.__bucho

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @bucho.setter
    def bucho(self, bucho):
        self.__bucho = bucho

    def comer(self,alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        print(f'{self.nome} esta com {self.bucho} no bucho.')

    def digerir(self,alimento):
        self.bucho.remove(alimento)

macaco1 = Macaco('Zangao')
macaco2 = Macaco('Doidao')

macaco1.comer('banana')
macaco1.comer('maca')
macaco1.comer('pera')

macaco2.comer('uva')
macaco2.comer('laranja')
macaco2.comer('morango')
macaco2.comer(macaco1)

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir('banana')
macaco1.verBucho()
macaco2.verBucho()