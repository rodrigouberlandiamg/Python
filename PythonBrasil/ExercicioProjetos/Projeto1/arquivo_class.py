class arquivo():
    def __init__(self):
        self.__nome_arquivo = "C:/Fontes/public/python/PythonBrasil/ExercicioProjetos/Projeto1/usuarios.txt"
        self.__nome_arquivo_dest = "C:/Fontes/public/python/PythonBrasil/ExercicioProjetos/Projeto1/relatorio.txt"

    @property
    def nome_arquivo(self):
        return self.__nome_arquivo

    @property
    def nome_arquivo_dest(self):
        return self.__nome_arquivo_dest

    def criar_lista_usuario(self):
        lista_usuario = []
        with open(self.nome_arquivo,'r') as arquivo:
            for linha in arquivo:
                lista_usuario.append([linha[0:15].rstrip(),linha[16:-1]])
        return lista_usuario

    def criar_relatorio(self,lista,espaco_total,media_total):
        i = 0
        with open(self.nome_arquivo_dest,'a+') as arquivo:
            arquivo.write('ACME Inc.           Uso do espaço em disco pelos usuários\n')
            arquivo.write('------------------------------------------------------------------------\n')
            arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
            for linha in lista:
                i += 1
                arquivo.write(f'{str(i)}  {str(linha[0])}        {str(linha[1])} MB     {str(linha[2])}%\n')
            arquivo.write(f'Espaço total ocupado: {str(round(espaco_total / 1024 / 1000, 2))} MB\n')
            arquivo.write(f'Espaço médio ocupado: {str(round(media_total / 1024, 2))} MB\n')