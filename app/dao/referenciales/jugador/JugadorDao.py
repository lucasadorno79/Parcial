# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class JugadorDao:

    def getJugadores(self):

        jugadorSQL = """
        SELECT id, descripcion
        FROM jugadores
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(jugadorSQL)
            jugadores = cur.fetchall()  # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': jugador[0], 'descripcion': jugador[1]} for jugador in jugadores]

        except Exception as e:
            app.logger.error(f"Error al obtener todos los jugadores: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getJugadorById(self, id):

        jugadorSQL = """
        SELECT id, descripcion
        FROM jugadores WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(jugadorSQL, (id,))
            jugadorEncontrado = cur.fetchone()  # Obtener una sola fila
            if jugadorEncontrado:
                return {
                    "id": jugadorEncontrado[0],
                    "descripcion": jugadorEncontrado[1]
                }  # Retornar los datos del jugador
            else:
                return None  # Retornar None si no se encuentra el jugador
        except Exception as e:
            app.logger.error(f"Error al obtener jugador: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarJugador(self, descripcion):

        insertJugadorSQL = """
        INSERT INTO jugadores(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertJugadorSQL, (descripcion,))
            jugador_id = cur.fetchone()[0]
            con.commit()  # se confirma la insercion
            return jugador_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar jugador: {str(e)}")
            con.rollback()  # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateJugador(self, id, descripcion):

        updateJugadorSQL = """
        UPDATE jugadores
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateJugadorSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount  # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0  # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar jugador: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteJugador(self, id):

        deleteJugadorSQL = """
        DELETE FROM jugadores
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteJugadorSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar jugador: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()