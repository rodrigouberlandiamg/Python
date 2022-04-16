# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#
#     Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade;
#     Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em
#     consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos
#     Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar
#     esta informação por que ela pode ser calculada a qualquer momento.

class BichinhoVirtual:
    def __init__(self,nome,fome,saude,idade):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def fome(self):
        return self.__fome

    @property
    def saude(self):
        return self.__saude

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @fome.setter
    def fome(self, fome):
        self.__fome = fome

    @saude.setter
    def saude(self, saude):
        self.__saude = saude

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def humor(self):
        return (self.fome+self.saude)/2

    def __str__(self):
        return f'Nome: {self.nome} \nFome: {self.fome} \nSaude: {self.saude} \nIdade: {self.idade}\nHumor: {self.humor()}'

tamagushi = BichinhoVirtual('Bixinho1',5,8,1)
print(tamagushi)

