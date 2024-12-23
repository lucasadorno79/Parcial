from datetime import timedelta 
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

#Crear token
crsf = CSRFProtect()
crsf.init_app(app)

#Inicializar secret key
app.secret_key = b'_5#y2L"F6Q7z\n\xec]'

#Establecer duracion de sesion, 15 minutos
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)

#Importar modulo de seguridad
from app.rutas.seguridad.login_routes import logmod
app.register_blueprint(logmod)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.equipo.equipo_routes import equmod
from app.rutas.referenciales.sucursal.sucursal_routes import sucurmod
from app.rutas.referenciales.jugador.jugador_routes import jugmod
from app.rutas.referenciales.pedido.pedido_routes import pedmod
from app.rutas.referenciales.departamento.departamento_routes import depmod
from app.rutas.referenciales.empleado.empleado_routes import empmod
from app.rutas.referenciales.factura.factura_routes import facmod
from app.rutas.referenciales.materia_prima.materia_prima_routes import matmod
from app.rutas.referenciales.categoria.categoria_routes import catmod
from app.rutas.referenciales.producto.producto_routes import promod
from app.rutas.referenciales.etapa_produccion.etapa_produccion_routes import etpmod
from app.rutas.gestionar_costos.registrar_costos.costo_routes import cosmod
from app.rutas.gestionar_etapa_produccion.registrar_etapa_produccion.registro_etapa_produccion_routes import repmod

# registrar referenciales
modulo0 = '/referenciales'

app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(equmod, url_prefix=f'{modulo0}/equipo')
app.register_blueprint(sucurmod, url_prefix=f'{modulo0}/sucursal')
app.register_blueprint(jugmod, url_prefix=f'{modulo0}/datosjugador')
app.register_blueprint(pedmod, url_prefix=f'{modulo0}/pedido')
app.register_blueprint(depmod, url_prefix=f'{modulo0}/departamento')
app.register_blueprint(empmod, url_prefix=f'{modulo0}/empleado')
app.register_blueprint(facmod, url_prefix=f'{modulo0}/factura')
app.register_blueprint(matmod, url_prefix=f'{modulo0}/materia_prima')
app.register_blueprint(catmod, url_prefix=f'{modulo0}/categoria')
app.register_blueprint(promod, url_prefix=f'{modulo0}/producto')
app.register_blueprint(etpmod, url_prefix=f'{modulo0}/etapa_produccion')
app.register_blueprint(cosmod, url_prefix=f'{modulo0}/registrar_costos')
app.register_blueprint(repmod, url_prefix=f'{modulo0}/registrar_etapa_produccion')

# importar gestionar compras
from app.rutas.gestionar_compras.registrar_pedido_compras.registrar_pedidos_compras_routes \
    import pdcmod

# registro de modulos - gestionar compras
modulo1 = '/gestionar-compras'
app.register_blueprint(pdcmod, url_prefix=f'{modulo1}/registrar-pedido-compras')

from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.persona.persona_api import perapi
from app.rutas.referenciales.pais.pais_api import paiapi
from app.rutas.referenciales.equipo.equipo_api import equapi
from app.rutas.referenciales.sucursal.sucursal_api import sucapi
from app.rutas.referenciales.jugador.jugador_api import jugapi
from app.rutas.referenciales.pedido.pedido_api import pedapi
from app.rutas.referenciales.departamento.departamento_api import depapi
from app.rutas.referenciales.empleado.empleado_api import empapi
from app.rutas.referenciales.factura.factura_api import facapi
from app.rutas.referenciales.materia_prima.materia_prima_api import matapi
from app.rutas.referenciales.categoria.categoria_api import catapi
from app.rutas.referenciales.producto.producto_api import proapi
from app.rutas.referenciales.etapa_produccion.etapa_produccion_api import etpapi
from app.rutas.gestionar_compras.registrar_pedido_compras.registrar_pedido_compras_api \
    import pdcapi
from app.rutas.gestionar_costos.registrar_costos.costo_api import cosapi
from app.rutas.gestionar_etapa_produccion.registrar_etapa_produccion.registro_etapa_produccion_api import repapi
# APIS v1
version1 = '/api/v1'

app.register_blueprint(ciuapi, url_prefix=version1)
app.register_blueprint(perapi, url_prefix=version1)
app.register_blueprint(paiapi, url_prefix=version1)
app.register_blueprint(equapi, url_prefix=version1)
app.register_blueprint(sucapi, url_prefix=version1)
app.register_blueprint(jugapi, url_prefix=version1)
app.register_blueprint(pedapi, url_prefix=version1)
app.register_blueprint(depapi, url_prefix=version1)
app.register_blueprint(empapi, url_prefix=version1)
app.register_blueprint(facapi, url_prefix=version1)
app.register_blueprint(matapi, url_prefix=version1)
app.register_blueprint(catapi, url_prefix=version1)
app.register_blueprint(proapi, url_prefix=version1)
app.register_blueprint(etpapi, url_prefix=version1)
app.register_blueprint(cosapi, url_prefix=version1)

# Gestionar compras API
app.register_blueprint(pdcapi, url_prefix=f'{version1}/{modulo1}/registrar-pedido-compras')