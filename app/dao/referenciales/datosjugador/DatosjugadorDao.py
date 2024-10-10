# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class DatosjugadorDao:

    def getDatosjugador(self):

        datosjugadorSQL = """
        SELECT id, descripcion
        FROM datosjugador
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(datosjugadorSQL)
            datosjugadores = cur.fetchall()  # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': datosjugador[0], 'descripcion': datosjugador[1]} for datosjugador in datosjugadores]

        except Exception as e:
            app.logger.error(f"Error al obtener todos los datos de jugadores: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getDatosjugadorById(self, id):

        datosjugadorSQL = """
        SELECT id, descripcion
        FROM datosjugador WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(datosjugadorSQL, (id,))
            datosjugadorEncontrado = cur.fetchone()  # Obtener una sola fila
            if datosjugadorEncontrado:
                return {
                    "id": datosjugadorEncontrado[0],
                    "descripcion": datosjugadorEncontrado[1]
                }  # Retornar los datos del jugador
            else:
                return None  # Retornar None si no se encuentra el dato del jugador
        except Exception as e:
            app.logger.error(f"Error al obtener dato de jugador: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarDatosjugador(self, descripcion):

        insertDatosjugadorSQL = """
        INSERT INTO datosjugador(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertDatosjugadorSQL, (descripcion,))
            datosjugador_id = cur.fetchone()[0]
            con.commit()  # se confirma la insercion
            return datosjugador_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar dato de jugador: {str(e)}")
            con.rollback()  # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateDatosjugador(self, id, descripcion):

        updateDatosjugadorSQL = """
        UPDATE datosjugador
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateDatosjugadorSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount  # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0  # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar dato de jugador: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteDatosjugador(self, id):

        deleteDatosjugadorSQL = """
        DELETE FROM datosjugador
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteDatosjugadorSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar dato de jugador: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()
