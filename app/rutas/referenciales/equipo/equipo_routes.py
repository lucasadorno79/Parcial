from flask import Blueprint, render_template

equmod = Blueprint('equipo', __name__, template_folder='templates')

@equmod.route('/equipo-index')
def equipoIndex():
    return render_template('equipo-index.html')