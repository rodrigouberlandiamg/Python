# Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a
# classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça
# um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método
# adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que
# construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois
# aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
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
        return round(self.__saldo,2)

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


class ContaInvestimento(ContaCorrente):
    def __init__(self,conta,nome,saldo,taxa_juros=0):
        super().__init__(conta,nome,saldo)
        self.__taxa_juros = taxa_juros

    @property
    def taxa_juros(self):
        return self.__taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, taxa_juros):
        self.__taxa_juros = taxa_juros

    def adicionaJuros(self,juros):
        self.saldo += (self.saldo*juros)/100


correntista = ContaInvestimento(123,'Rodrigo',1000,10)
print(correntista)
correntista.alteraNome('Rodrigo Silva Oliveira')
correntista.deposito(3000.00)
print(correntista)
correntista.saque(1100.00)
print(correntista)
correntista.adicionaJuros(10)
print(correntista)
correntista.adicionaJuros(10)
correntista.adicionaJuros(10)
correntista.adicionaJuros(10)
correntista.adicionaJuros(10)
print(correntista)