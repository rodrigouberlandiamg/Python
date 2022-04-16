# Letra maiuscula no começo do nome da classe e cada palavra.
# self = referencia de onde encontrar o objeto.
# __ Encapsulamento self.__atributo serve para atributos e metodos
# Classe deve ter uma responsabilidade deve ser coesa.
# Métodos Estaticos @staticmethod
#Construtor
class Conta:
    def __init__(self,numero,titular,saldo,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f'Saldo {self.__titular} é de R${self.__saldo}.')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'Não tem limite diponível para sacar R${valor}.')

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    #Método estatico da classe
    @staticmethod
    def codigo_banco():
        #return '001'
        return {'BB':'001','Caixa':'104','Bradesco':'237'}