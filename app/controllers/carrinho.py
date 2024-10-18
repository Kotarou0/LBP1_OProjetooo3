from flask import Flask, Blueprint, render_template, request, redirect, url_for, make_response
from models import produtos

c = Blueprint('carrinho', __name__)

@c.route('/carrinho/add') # type: ignore
def add():
    id = request.args.get('id')
    resp = make_response()
    valor = 'oi'
    resp.set_cookie(f'produto_{id}', valor)