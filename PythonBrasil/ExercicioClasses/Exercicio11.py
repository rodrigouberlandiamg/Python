# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
#
#     Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
#     quantidade de combustível no tanque.
#     O consumo é especificado no construtor e o nível de combustível inicial é 0.
#     Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
#     reduzindo o nível de combustível no tanque de gasolina.
#     Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
#     Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
#
#     meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
#     meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
#     meuFusca.andar(100);            # anda 100 quilômetros.
#     meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.


class Carro:
    def __init__(self,consumo,nivel=0):
        self.__consumo = consumo
        self.__nivel = nivel

    @property
    def consumo(self):
        return self.__consumo

    @property
    def nivel(self):
        return self.__nivel

    @consumo.setter
    def consumo(self,consumo):
        self.__consumo = consumo

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    def andar(self,distancia):
        self.nivel = distancia/self.consumo

    def obterGasolina(self):
        return self.nivel

    def adicionarGasolina(self,quantidade):
        self.nivel += quantidade

meuFusca = Carro(15)           # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20) # abastece com 20 litros de combustível.
meuFusca.andar(100)            # anda 100 quilômetros.
print(meuFusca.obterGasolina())        # Imprime o combustível que resta no tanque.