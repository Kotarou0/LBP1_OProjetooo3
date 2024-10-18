from flask import Flask, Blueprint, render_template, request, redirect, url_for, abort
from models import sessoes

c = Blueprint('admin', __name__)

@c.route('/admin')
def admin_page():
    if sessoes.get('tipo') != 'admin': abort(401)
    return render_template('admin.html')