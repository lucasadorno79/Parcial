from flask import current_app as app
from app.conexion.Conexion import Conexion

class PersonaDao:

    def getPersonas(self):

        personaSQL = """
        SELECT id, nombre, direccion, telefono, sexo
        FROM personas
        """
        #Objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL)
            personas = cur.fetchall() #trae los datos de la base de datos

            #Transformar los datos en una lista de diccionarios
            return[{"id": persona[0], "nombre": persona[1], 'direccion': persona[2],
            'telefono':persona[3], 'correo_electronico': persona[4], 'sexo': persona[5]} for persona in personas] 
        except Exception as e:
            app.logger.error(f"Error al obtener todas las personas: {str(e)}")
            return[]
        finally:
            cur.close()
            con.close()


    def getPersonaById(self, id): #definicion de la funcion
         #definicion de la consulta SQL
        personaSQL = """            
        SELECT id, nombre, direccion, telefono, correo_electronico, sexo
        FROM personas WHERE id=%s
        """
        #Establecer la conexion a la base de datos
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    #Ejecucion y respuesta de la consulta SQL
            cur.execute(personaSQL, (id,))
            personaEncontrada = cur.fetchone()
            if personaEncontrada:       #Verificacion y retorno de datos
                return{
                    "id": personaEncontrada[0],
                    "nombre": personaEncontrada[1],
                    "direccion": personaEncontrada[2],
                    "telefono": personaEncontrada[3],
                    "correo_electronico": personaEncontrada[4],
                    "sexo": personaEncontrada[5]

                } 
            else:
                return None
            #Manejo de excepciones
        except Exception as e:
            app.logger.error(f"Error al obtener persona: {str(e)}")
            return None
        #CIerre de la conexion
        finally:
            cur.close()
            con.close()

    def guardarPersona(self, nombre, direccion, telefono, correo_electronico, sexo):

        insertPersonaSQL = """
        INSERT INTO personas(nombre, direccion, telefono, correo_electronico, sexo)
        VALUES(%s, %s, %s, %s, %s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertPersonaSQL,(nombre, direccion, telefono, correo_electronico, sexo,))
            persona_id = cur.fetchone()[0]
            con.commit()
            return persona_id
        

        except Exception as e:
            app.logger.error(f"Error al insertar persona: {str(e)}")
            con.rollback()
            return False
        
        finally:
            cur.close()
            con.close()

    def updatePersona(self, id, nombre, direccion, telefono, correo_electronico, sexo):        

        updatePersonaSQL = """
        UPDATE personas
        SET nombre=%s, direccion=%s, telefono=%s, correo_electronico=%s, sexo=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePersonaSQL, (nombre, direccion, telefono, correo_electronico, sexo, id,))
            filas_afectadas = cur.rowcount
            con.commit()

            return filas_afectadas > 0
        
        except Exception as e:
            app.logger.error(f"Error al actualizar persona: {str(e)}")
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    def deletePersona(self, id):

        updatePersonaSQL = """
        DELETE FROM personas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePersonaSQL, (id))
            rows_affectd = cur.rowcount
            con.commit()

            return rows_affectd > 0

        except Exception as e:
            app.logger.error(f"Error al eliminar persona: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()        