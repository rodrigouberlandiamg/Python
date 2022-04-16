from arquivo_class import arquivo

class calculo(arquivo):
    def __init__(self):
        super().__init__()

    def media_total(self):
        lista = self.criar_lista_usuario()
        media = 0
        for linha in lista:
            media += float(linha[1])
        return (media / len(lista))/1024

    def espaco_total(self):
        lista = self.criar_lista_usuario()
        total = 0
        for linha in lista:
            total += float(linha[1])
        return total

    def media_usuario(self,total_utilizado):
        lista = self.criar_lista_usuario()
        nova_lista = []
        for linha in lista:
            nova_lista.append([linha[0],round(float(linha[1])/1024/1000,2),round((float(linha[1])*100)/total_utilizado,2)])
        return nova_lista
