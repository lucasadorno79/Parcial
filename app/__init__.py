from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.cliente.cliente_routes import climod
from app.rutas.referenciales.cargo.cargo_routes import carmod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocumod
from app.rutas.referenciales.equipo.equipo_routes import equmod
from app.rutas.referenciales.sucursal.sucursal_routes import sucmod
from app.rutas.referenciales.datosjugador.datosjugador_routes import datmod
from app.rutas.referenciales.pago.pago_routes import pagmod
from app.rutas.referenciales.vehiculo.vehiculo_routes import vehmod
from app.rutas.referenciales.pedido.pedido_routes import pedmod
from app.rutas.referenciales.departamento.departamento_routes import depmod
from app.rutas.referenciales.empleado.empleado_routes import empmod
from app.rutas.referenciales.factura.factura_routes import facmod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(climod, url_prefix=f'{modulo0}/cliente')
app.register_blueprint(carmod, url_prefix=f'{modulo0}/cargo')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(nacmod, url_prefix=f'{modulo0}/nacionalidad')
app.register_blueprint(ocumod, url_prefix=f'{modulo0}/ocupacion')
app.register_blueprint(equmod, url_prefix=f'{modulo0}/equipo')
app.register_blueprint(sucmod, url_prefix=f'{modulo0}/sucursal')
app.register_blueprint(datmod, url_prefix=f'{modulo0}/datosjugador')
app.register_blueprint(pagmod, url_prefix=f'{modulo0}/pago')
app.register_blueprint(vehmod, url_prefix=f'{modulo0}/vehiculo')
app.register_blueprint(pedmod, url_prefix=f'{modulo0}/pedido')
app.register_blueprint(depmod, url_prefix=f'{modulo0}/departamento')
app.register_blueprint(empmod, url_prefix=f'{modulo0}/empleado')
app.register_blueprint(facmod, url_prefix=f'{modulo0}/factura')






from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.cliente.cliente_api import cliapi
from app.rutas.referenciales.cargo.cargo_api import carapi
from app.rutas.referenciales.pais.pais_api import paiapi
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacapi
from app.rutas.referenciales.ocupacion.ocupacion_api import ocuapi
from app.rutas.referenciales.equipo.equipo_api import equapi
from app.rutas.referenciales.sucursal.sucursal_api import sucapi
from app.rutas.referenciales.datosjugador.datosjugador_api import datapi
from app.rutas.referenciales.pago.pago_api import pagapi
from app.rutas.referenciales.vehiculo.vehiculo_api import vehapi
from app.rutas.referenciales.pedido.pedido_api import pedapi
from app.rutas.referenciales.departamento.departamento_api import depapi
from app.rutas.referenciales.empleado.empleado_api import empapi
from app.rutas.referenciales.factura.factura_api import facapi
# APIS v1
version1 = '/api/v1'

app.register_blueprint(ciuapi, url_prefix=version1)
app.register_blueprint(cliapi, url_prefix=version1)
app.register_blueprint(carapi, url_prefix=version1)
app.register_blueprint(paiapi, url_prefix=version1)
app.register_blueprint(nacapi, url_prefix=version1)
app.register_blueprint(ocuapi, url_prefix=version1)
app.register_blueprint(equapi, url_prefix=version1)
app.register_blueprint(sucapi, url_prefix=version1)
app.register_blueprint(datapi, url_prefix=version1)
app.register_blueprint(pagapi, url_prefix=version1)
app.register_blueprint(vehapi, url_prefix=version1)
app.register_blueprint(pedapi, url_prefix=version1)
app.register_blueprint(depapi, url_prefix=version1)
app.register_blueprint(empapi, url_prefix=version1)
app.register_blueprint(facapi, url_prefix=version1)
