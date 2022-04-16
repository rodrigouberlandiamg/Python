#super().__init__(nome, ano) - (extenção) nas classes filhas para chamar atributos e metodos da classe mae

# Veja os 3 métodos das classes mãe e filhas imprimir() (Polimorfismo) onde  quando fazemos o FOR não importa
# qual objeto esta sendo acessado.
# Utilização do __str__ para imprimir idependente do objeto substituindo a descrição acima.
# Representação textual do objeto.

class Programa:
    def __init__(self,nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @likes.setter
    def likes(self, likes):
        self._likes = likes

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} likes.'

    #    def imprimir(self):
    #        print(f'{self.nome} - {self.ano} - {self.likes} likes.')

class Filme(Programa):
    def __init__(self,nome, ano,duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min. - {self.likes} likes.'


class Series(Programa):
    def __init__(self,nome, ano,temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} - {self.likes} likes.'

# Herança de built-in
class Playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas
    #    def __init__(self,nome,programas):
    #        self.nome = nome
    #        super().__init__(programas)

    # Pega os itens do objeto (comportamento)
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    # __len__ podemos verificar o tamanho da lista.
    def __len__(self):
        return len(self._programas)
#    @property
#    def tamanho(self):
#        return len(self._programas)

#from modelo import Filme, Series

atlanta = Series('Atlanta',2018,2)
demolidor = Series('Demolidor',1980,3)
vingadores = Filme('Vingadores - Guerra Infinita',2018,160)
tmep = Filme('todo mundo em panico',2010,200)
atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()
demolidor.dar_like()
tmep.dar_like()
#print(f'{vingadores.nome} - {vingadores.duracao} - {vingadores.likes}')
#print(f'{atlanta.nome} - {atlanta.temporadas} - {atlanta.likes}')

filmes_e_series = [vingadores,atlanta,demolidor,tmep]
playlist_fim_de_semana = Playlist('Fim de semana,',filmes_e_series)

'''for programa in filmes_e_series:
    # hasattr - verifica se existe o atributo no objeto.
    detalhes = programa.duracao if hasattr(programa,'duracao') else programa.temporadas
    print(f'{programa.nome} - {detalhes} - {programa.likes}')'''

#print(f'Tamanho da Playlist: {len(playlist_fim_de_semana.listagem)}')
print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tá na lista? {demolidor in playlist_fim_de_semana.listagem}')

print(demolidor in playlist_fim_de_semana)
print(playlist_fim_de_semana[1])

'''
thander pythonicos - Convertes objeto em ...

- Inicialização - __init__
- Representação - __str__, __repr__
- Container, sequencia - __contains__, __iter__, __len__, __getitem__
- Numericos - __add__, __sub__, __mul__, __mod__

'''