from flask import Blueprint, render_template

vehmod = Blueprint('vehiculo', __name__, template_folder='templates')

@vehmod.route('/vehiculo-index')
def vehiculoIndex():
    return render_template('vehiculo-index.html')