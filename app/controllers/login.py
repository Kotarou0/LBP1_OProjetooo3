from flask import Flask, Blueprint, render_template, request, redirect, url_for
from models import usuarios, sessoes

c = Blueprint('login', __name__)
sucesso_login = True

@c.route('/login', methods=['POST', 'GET']) # type: ignore
def login():
    global sucesso_login
    if request.method == 'GET':
        if not sessoes.existe('nome'):
            return render_template('login.html', sl=sucesso_login)
        else:
            return redirect(url_for('index'))
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        for u in usuarios.USUARIOS:
            if nome == u.nome and senha == u.senha:
                sucesso_login = True
                sessoes.atualizar_login('nome', nome)
                sessoes.atualizar_login('tipo', u.tipo)
                return redirect(url_for('index'))
        
        sucesso_login = False
        return redirect(url_for('login.login'))

@c.route('/logout')
def logout():
    sessoes.limpar_login()
    return redirect(url_for('index'))
