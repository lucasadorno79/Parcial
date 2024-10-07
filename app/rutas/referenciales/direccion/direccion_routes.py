from flask import Blueprint, render_template

dirmod = Blueprint('direccion', __name__, template_folder='templates')

@dirmod.route('/direccion-index')
def direccionIndex():
    return render_template('direccion-index.html')