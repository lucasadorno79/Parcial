from flask import Blueprint, render_template

jugmod = Blueprint('jugador-index', __name__, template_folder='templates')

@jugmod.route('/jugador-index')
def jugadorIndex():
    return render_template('jugador-index.html')