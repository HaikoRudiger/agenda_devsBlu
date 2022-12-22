from flask import render_template, request, redirect, flash, url_for,session
from main import db, app
from models.evento import Evento
from models.usuario import Usuario

@app.route("/")
def index():

    return render_template("index.html", titulo = "Agenda de Eventos")


@app.route("/login")
def login():
    proximo = request.args.get("proximo")

    return render_template("login.html", proximo = proximo)


@app.route("/autenticar", methods = ["post"])
def autenticar():
    usuario = Usuario.query.filter_by(username = request.form["nome"]).first()

    if usuario:
        if request.form["senha"] == usuario.senha:
            session["usuario_logado"] = usuario.username
            flash(usuario.username + " Usuário logado com sucesso.")

            proxima_pagina = request.form["proximo"]

            return redirect(proxima_pagina)

        else:
            flash("Usuário ou senha incorretos.")

            return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["usuario_logado"] == None
    flash("Você foi desconectado.")

    return redirect(url_for("login"))
    # Ou retorna para a página principal ou para a página de Login


@app.route("/novo_usuario")
def novo_usuario():

    return render_template("cadastro_usuario.html", titulo = "Criar novo Usuário")


@app.route("/cadastrar_usuario", methods = ["POST"])
def cadastrar_usuario():
    
    username = request.form["username"]
    nome = request.form["nome"]
    senha = request.form["senha"]

    usuario = Usuario.query.filter_by(username = username).first()
    
    if usuario:
        flash("Usuário já cadastrado")

        return redirect(url_for("index"))

    novo_usuario = Usuario(username = username, nome = nome, senha = senha)

    db.session.add(novo_usuario)

    db.session.commit()

    return redirect(url_for("index"))
