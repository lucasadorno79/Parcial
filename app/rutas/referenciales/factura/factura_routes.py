from flask import Blueprint, render_template

facmod = Blueprint('factura', __name__, template_folder='templates')

@facmod.route('/factura-index')
def facturaIndex():
    return render_template('factura-index.html')