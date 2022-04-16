# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
# (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
#
#     Exemplo de uso:
#
#       harry=funcionário("Harry",25000)
#       harry.aumentarSalario(10)

class Funcionario:
    def __init__(self, nome, salario=0.00):
        self.__nome = nome
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return float(self.__salario)

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @salario.setter
    def salario(self, salario):
        self.__salario = float(salario)

    def __str__(self):
        return f'Nome: {self.nome} tem sário de R${str(self.__salario)}'

    def aumentarSalario(self,percentual):
        self.salario += (self.salario*percentual)/100

funcionario = Funcionario('Rodrigo', 8000)
funcionario.aumentarSalario(10)
print(funcionario)