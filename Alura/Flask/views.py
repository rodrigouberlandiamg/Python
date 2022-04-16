import time
from flask import render_template,request, redirect,session,flash,url_for,send_from_directory
from models import Jogo
from dao import JogoDao,UsuarioDao
from jogoteca import db,app
from helpers import deleta_arquivo,recupera_imagem
jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    # Retornando um html escrito no python
    # return '<h1>Olá Flask</h1>'
    # Criando um alista de jogos.
    # lista = ['Tetris','Street Figther','Need For Speed','Mortal Kombat']
    lista = jogo_dao.listar()
    #Retornando um html escrito em arquivo. Veja que titulo é uma variavel que esta no codigo HTML
    return render_template('lista.html', titulo='Jogos',jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novo')))
    return render_template('novo.html',titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo = jogo_dao.salvar(jogo)
    #lista.append(jogo)
    #return render_template('lista.html',titulo='Jogo',jogos=lista)
    jogo_dao.salvar(jogo)

    # Salvar a Imagem
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}\\capa_{jogo.id}-{timestamp}.jpg')
    # Redirecionar para outra pagina.
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('editar')))
    jogo = jogo_dao.busca_por_id(id)
    nome_imagem = recupera_imagem(id)
    return render_template('editar.html',titulo='Editando Jogo', jogo=jogo, capa_jogo=nome_imagem)

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('editar')))
    jogo_dao.deletar(id)
    flash('Jogo deletado com sucesso.')
    return redirect(url_for('index'))

@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console, id=request.form['id'])
    # lista.append(jogo)
    # return render_template('lista.html',titulo='Jogo',jogos=lista)
    jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    deleta_arquivo(jogo.id)
    timestamp = time.time()
    arquivo.save(f'{upload_path}\\capa_{jogo.id}-{timestamp}.jpg')
    # Redirecionar para outra pagina.
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logado com sucesso.')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Não logado. Tente novamente.')
            return redirect(url_for('login'))
    else:
        flash('Não logado. Tente novamente.')
        return redirect(url_for('login'))
    # if 'mestra' == request.form['senha']:
    #     session['usuario_logado'] = request.form['usuario']
    #     flash(request.form['usuario']+' logado com sucesso.')
    #     proxima_pagina = request.form['proxima']
    #     return redirect(proxima_pagina)
    # else:
    #     flash('Não logado. Tente novamente.')
    #     return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!.')
    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads',nome_arquivo)