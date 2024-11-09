from flask import current_app as app
from app.conexion.Conexion import Conexion

class PersonasDao:

    def getPersonas(self):

        personasql = """
        SELECT id, descripcion
        FROM ciudades
        """