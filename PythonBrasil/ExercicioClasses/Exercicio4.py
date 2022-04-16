# Classe Pessoa: Crie uma classe que modele uma pessoa:
#
#     Atributos: nome, idade, peso e altura
#     Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa
#     pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self,nome,idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def peso(self):
        return self.__peso
    @property
    def altura(self):
        return self.__altura

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.05

    def engordar(self,peso_mais):
        self.peso += peso_mais

    def emagrecer(self,peso_menos):
        self.peso -= peso_menos

    def crescer(self,altura_mais):
        self.altura += altura_mais

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Peso de {self.peso} e altura de {self.altura} metros.'

pessoa = Pessoa('Julia Maria',14,35,1.60)
pessoa.emagrecer(5)
pessoa.engordar(6)
pessoa.crescer(0.05)
pessoa.envelhecer()
print(pessoa)
