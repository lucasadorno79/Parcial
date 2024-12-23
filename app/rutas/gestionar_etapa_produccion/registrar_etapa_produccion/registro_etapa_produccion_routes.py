from flask import Blueprint, render_template

repmod = Blueprint('registro_etapa_produccion', __name__, template_folder='templates')

@repmod.route('/registro_etapa_produccion-index')
def registro_etapa_produccionIndex():
    return render_template('registro_etapa_produccion-index.html')