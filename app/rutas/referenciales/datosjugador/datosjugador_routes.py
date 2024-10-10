from flask import Blueprint, render_template

datmod = Blueprint('datosjugador-index', __name__, template_folder='templates')

@datmod.route('/datosjugador-index')
def datosjugadorIndex():
    return render_template('datosjugador-index.html')