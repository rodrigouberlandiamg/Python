# Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome
# (um string) e um salário(um double). Escreva um construtor com dois parâmetros
# (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que
# teste sua classe.

class Funcionario:
    def __init__(self,nome,salario=0.00):
        self.__nome = nome
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return float(self.__salario)

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @salario.setter
    def salario(self,salario):
        self.__salario = float(salario)

    def __str__(self):
        return f'Nome: {self.nome} tem sário de R${str(self.__salario)}'

funcionario = Funcionario('Rodrigo',8000)
print(funcionario)