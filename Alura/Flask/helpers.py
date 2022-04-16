import os
from jogoteca import app


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}' in nome_arquivo:
            return nome_arquivo
    return 'capa_padrao.jpg'


    # if os.path.isfile(os.path.join(app.config['UPLOAD_PATH'], f'capa_{id}.jpg')):
    #     print(os.path.join(app.config['UPLOAD_PATH'], f'capa_{id}.jpg'))
    #     return f'capa_{id}.jpg'
    # # else:
    #     print(os.path.join(app.config['UPLOAD_PATH'], 'capa_padrao.jpg'))
    #     return 'capa_padrao.jpg'
    # for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
    #     if f'capa_{id}' in nome_arquivo:
    #         return os.path.join(app.config['UPLOAD_PATH'],nome_arquivo)


def deleta_arquivo(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}' in nome_arquivo:
            os.remove(os.path.join(app.config['UPLOAD_PATH'], nome_arquivo))