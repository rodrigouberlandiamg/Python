# Classe Retangulo: Crie uma classe que modele um retangulo:
#
#     Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#     Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#     Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
#     de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos
#     e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self,ladoa=0,ladob=0):
        self.__ladoa = ladoa
        self.__ladob = ladob

    @property
    def ladoa(self):
        return self.__ladoa

    @property
    def ladob(self):
        return self.__ladob

    @ladoa.setter
    def ladoa(self,ladoa):
        self.__ladoa = ladoa

    @ladob.setter
    def ladob(self, ladob):
        self.__ladob = ladob

    def mudar_valor_lados(self,novo_valora,novo_valorb):
        self.ladoa = novo_valora
        self.ladob = novo_valorb

    def retorna_valor_lados(self):
        return [self.ladoa,self.ladob]

    def calcula_area(self):
        return self.ladoa * self.ladob

    def calcula_perimetro(self):
        return (self.ladoa*2) + (self.ladob*2)


area = Retangulo()
base = float(input('Entre com a medida da base: '))
altura = float(input('Entre com a medida da altura: '))
area.mudar_valor_lados(base,altura)
print(f'Valor dos lados: {area.retorna_valor_lados()}')
print(f'Calcula da area do retangulo: {area.calcula_area()}')
print(f'Calcula da area do perimetro: {area.calcula_perimetro()}')

area_piso = Retangulo()
base = float(input('Entre com a medida da base do piso: '))
altura = float(input('Entre com a medida da altura do piso: '))
area_piso.mudar_valor_lados(base,altura)
print(area_piso.calcula_area())
tamanho_rodape = float(input('Entre com a altura do rodapé: '))
print(f'A quantidade de pisos necessárias é de {(area.calcula_area()/area_piso.calcula_area())+((area_piso.ladob/tamanho_rodape)*area_piso.calcula_perimetro())}')