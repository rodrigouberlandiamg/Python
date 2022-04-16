# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self,conta,nome,saldo=0.00):
        self.__conta = conta
        self.__nome = nome
        self.__saldo = saldo

    @property
    def conta(self):
        return self.__conta

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @conta.setter
    def conta(self,conta):
        self.__conta = conta

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    def __str__(self):
        return f'Nome: {self.nome}, conta: {self.conta}, saldo de R${self.saldo}.'

    def alteraNome(self,novo_nome):
        self.nome = novo_nome

    def deposito(self,valor):
        self.saldo += valor

    def saque(self,valor):
        self.saldo -= valor

correntista = ContaCorrente(123,'Rodrigo')
print(correntista)
correntista.alteraNome('Rodrigo Silva Oliveira')
correntista.deposito(3000.00)
print(correntista)
correntista.saque(1100.00)
print(correntista)