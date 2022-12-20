from flask import render_template, request, redirect, flash, url_for,session
from main import db, app
from models.evento import Evento
from models.usuario import Usuario

@app.route('/index')
def index():
    return redirect(url_for('index'))

@app.route('/novo-usuario')
def novo():
    return render_template('cadastro-usuario.html', titulo = 'Criar Novo Usuário')

@app.route('/cadastrar-usuario', methods = ['POST'])
def cadastro_usuario():

    nome = request.form['nome']
    userName = request.form['username']
    senha = request.form['senha'] #ver com a parte do Jean.

    usuario = Usuario.query.filter_by('username' = userName).first()
    
    if usuario:
        flash('Usuário já cadastrado')
        return redirect(url_for('index'))
    
    novo_usuario = Usuario('nome' = nome, 'username' = userName, 'senha' = senha)
    
    db.session.add(novo_usuario)

    db.session.commit()

    return redirect(url_for(index))

#url_for chama a função.
# nome, hora e descrição
# nome de usuario e senha

@app.route('/login')
def login():
#Jean

@app.route('/autenticar')
def autenticacao():
#Jean

@app.route('/cadastrar-evento')
def cadastrar_evento():
    
    data_evento = request.form['data_evento']
    titulo_evento = request.form['titulo_evento']
    descricao_evento = request.form['descricao_evento']
    publico = request.form['publico']
    ativo = request.form['ativo']

    evento = Evento.query.filter_by('data_evento' = data_evento).first()
    
    if evento:
        flash('Já existe um evento nessa data')
        return redirect(url_for('calendario'))

    novo_evento = Evento('data_evento' = data_evento, 'titulo_evento' = titulo_evento, 'descricao_evento' = descricao_evento, 'publico' = publico, 'ativo' = ativo)
    
    db.session.add(novo_evento)

    db.session.commit()

    return redirect(url_for('calendario'))

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/editar/<int:id>')
def editar(id):

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo = url_for('editar')))
    evento = Evento.query.filter_by(id=id).first() #verificar qual é o ID que virá, se é do usuário ou do evento.
    return render_template('HTML DO EDITAR - COLOCAR AQUI', titulo = 'Editar Evento', evento = evento)

@app.route('/deletar/<int:id>')
def deletar(id):

    if 'usuario_logado' not in session or session['usuario_logado' is None]:
        return redirect(url_for('login'))
    
    Evento.query.filter_by(id=id).delete()

    db.session.commit()

    flash('Evento deletado com sucesso')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Você foi desconectado")

    return redirect(url_for('login'))

