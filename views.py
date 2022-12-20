from flask import render_template, request, redirect, flash, url_for

@app.route('/index')
def index():

@app.route('/login')
def login():
#Jean

@app.route('/autenticar')
def autenticacao():
#Jean

@app.route('/cadastrar-evento')
def cadastrar_evento():

@app.route('/calendario')
def calendario():

@app.route('/editar/<int:id>')
def editar(id):

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo = url_for('editar')))
    evento = 

@app.route('/deletar')
def deletar():

@app.route('/logout')
def logout():

