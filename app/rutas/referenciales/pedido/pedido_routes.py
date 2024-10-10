from flask import Blueprint, render_template

pedmod = Blueprint('pedidos', __name__, template_folder='templates')

@pedmod.route('/pedidos-index')
def pedidosIndex():
    return render_template('pedidos-index.html')