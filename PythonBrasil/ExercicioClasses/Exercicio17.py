# Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o
# controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés
# de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda
# inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os
# bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os
# bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial
# aleatório de fome e tédio.

class BichinhoVirtual:
    def __init__(self,nome,fome,saude,idade,comida=0,tempo_brincar=0):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
        self.__comida = comida
        self.__tempo_brincar = tempo_brincar

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

    @property
    def comida(self):
        return self.__comida

    @property
    def tempo_brincar(self):
        return self.__tempo_brincar


    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @fome.setter
    def fome(self, fome):
        self.__fome = fome

    @saude.setter
    def saude(self, saude):
        self.__saude = saude

    @comida.setter
    def comida(self, comida):
        self.__comida = comida

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @tempo_brincar.setter
    def tempo_brincar(self, tempo_brincar):
        self.__tempo_brincar = tempo_brincar
        self.comida -= 1

    def humor(self):
        return (self.fome+self.saude)/2

    def dar_comida(self,comida):
        self.comida += comida
        self.fome -= comida

    def brinca(self,tempo):
        self.tempo_brincar += tempo

    def __str__(self):
        return f'Nome: {self.nome} \nFome: {self.fome} \nSaude: {self.saude} \nIdade: {self.idade}\nHumor: {self.humor()}\nTempo Brincando: {self.tempo_brincar}\nComida: {self.comida}'

tamagushi = BichinhoVirtual('Bixinho1',5,8,1)
tamagushi.dar_comida(2)
tamagushi.brinca(8)
tamagushi.dar_comida(3)
print(tamagushi)
