from flask import Flask, Blueprint, render_template
from models import m_1

c = Blueprint('carros', __name__)

@c.route('/carrinhos')
def octane():
    return render_template('carrinhos.html', carrinhos = m_1.carrinhos)