from flask import Flask, render_template, session, request, redirect, url_for
from controllers import login, admin, carrinho
from models import sessoes, produtos

app = Flask(__name__)
app.register_blueprint(login.c)
app.register_blueprint(admin.c)
app.register_blueprint(carrinho.c)
app.secret_key = 'senha super secreta'

@app.errorhandler(404)
def page_not_found(error):
    return 'Página não encontrada', 404

@app.errorhandler(401)
def acesso_negado(error):
    return 'Acesso negado!', 401

@app.before_request
def b4_request():
    if request.path == '/login':
        return
    if not sessoes.existe('nome'):
        return redirect(url_for('login.login'))

@app.after_request
def a_request(response):
    print("Depois da requisição")
    return response

@app.route('/')
def index():
    return render_template('index.html', nome=sessoes.get('nome'), produtos = produtos.LISTA_PRODUTOS)

if __name__ == '__main__':
    app.run(debug=True)