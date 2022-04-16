# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Tv:
    def __init__(self,canal=0,volume=0):
        self.__canal = canal
        self.__volume = volume

    @property
    def canal(self):
        return self.__canal

    @property
    def volume(self):
        return self.__volume

    @canal.setter
    def canal(self,canal):
        self.__canal = canal

    @volume.setter
    def volume(self,volume):
        self.__volume = volume

    def __str__(self):
        return f'CANAL: {self.canal} | VOLUME: {self.volume}'

    def seleciona_canal(self,canal):
        if canal < 0  or canal > 300:
            print(f'CANAL INVALIDO.')
        else:
            self.canal = canal

    def aumenta_volume(self):
        if self.volume > -1 and self.volume < 100:
            self.volume += 1

    def diminui_volume(self):
        if self.volume > 0 and self.volume <= 100:
            self.volume -= 1

televisao = Tv()
print(televisao)

for i in range(80):
    televisao.aumenta_volume()

for i in range(30):
    televisao.diminui_volume()


televisao.seleciona_canal(99)

print(televisao)