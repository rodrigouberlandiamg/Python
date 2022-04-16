# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
#
#     Possua uma classe chamada Ponto, com os atributos x e y.
#     Possua uma classe chamada Retangulo, com os atributos largura e altura.
#     Possua uma função para imprimir os valores da classe Ponto
#     Possua uma função para encontrar o centro de um Retângulo.
#     Você deve criar alguns objetos da classe Retangulo.
#     Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
#     retângulo, que deve ser um objeto da classe Ponto.
#     A função para encontrar o centro do retângulo deve retornar o valor para um objeto do
#     tipo ponto que indique os valores de x e y para o centro do objeto.
#     O valor do centro do objeto deve ser mostrado na tela
#     Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self,x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return f'x:{self.x} | y: {self.y}'


class Retangulo(Ponto):
    def __init__(self,largura,altura,x,y):
        super().__init__(x,y)
        self.__largura = largura
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self,largura):
        self.__largura = largura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def centro(self):
        print(f'x: {self.largura/2} e y: {self.altura/2}')

retangulo_inf_esq = Ponto(10,12)
