from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.cliente.cliente_routes import climod
from app.rutas.referenciales.cargo.cargo_routes import carmod
from app.rutas.referenciales.pais.pais_routes import paimod
from app.rutas.referenciales.direccion.direccion_routes import dirmod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocumod
from app.rutas.referenciales.equipo.equipo_routes import equmod
from app.rutas.referenciales.sucursal.sucursal_routes import sucmod
from app.rutas.referenciales.telefono.telefono_routes import telmod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(climod, url_prefix=f'{modulo0}/cliente')
app.register_blueprint(carmod, url_prefix=f'{modulo0}/cargo')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(dirmod, url_prefix=f'{modulo0}/direccion')
app.register_blueprint(nacmod, url_prefix=f'{modulo0}/nacionalidad')
app.register_blueprint(ocumod, url_prefix=f'{modulo0}/ocupacion')
app.register_blueprint(equmod, url_prefix=f'{modulo0}/equipo')
app.register_blueprint(sucmod, url_prefix=f'{modulo0}/sucursal')
app.register_blueprint(telmod, url_prefix=f'{modulo0}/telefono')





from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
from app.rutas.referenciales.cliente.cliente_api import cliapi
from app.rutas.referenciales.cargo.cargo_api import carapi
from app.rutas.referenciales.pais.pais_api import paiapi
from app.rutas.referenciales.direccion.direccion_api import dirapi
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacapi
from app.rutas.referenciales.ocupacion.ocupacion_api import ocuapi
from app.rutas.referenciales.equipo.equipo_api import equapi
from app.rutas.referenciales.sucursal.sucursal_api import sucapi
from app.rutas.referenciales.telefono.telefono_api import telapi


# APIS v1
version1 = '/api/v1'

app.register_blueprint(ciuapi, url_prefix=version1)
app.register_blueprint(cliapi, url_prefix=version1)
app.register_blueprint(carapi, url_prefix=version1)
app.register_blueprint(paiapi, url_prefix=version1)
app.register_blueprint(dirapi, url_prefix=version1)
app.register_blueprint(nacapi, url_prefix=version1)
app.register_blueprint(ocuapi, url_prefix=version1)
app.register_blueprint(equapi, url_prefix=version1)
app.register_blueprint(sucapi, url_prefix=version1)
app.register_blueprint(telapi, url_prefix=version1)
