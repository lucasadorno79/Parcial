# Data access object - DAO 
from flask import current_app as app
from app.conexion.Conexion import Conexion

class FacturaDao:

    def getFacturas(self):

        facturaSQL = """
        SELECT id, descripcion
        FROM facturas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(facturaSQL)
            facturas = cur.fetchall()  # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': factura[0], 'descripcion': factura[1]} for factura in facturas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las facturas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getFacturaById(self, id):

        facturaSQL = """
        SELECT id, descripcion
        FROM facturas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(facturaSQL, (id,))
            facturaEncontrada = cur.fetchone()  # Obtener una sola fila
            if facturaEncontrada:
                return {
                    "id": facturaEncontrada[0],
                    "descripcion": facturaEncontrada[1]
                }  # Retornar los datos de la factura
            else:
                return None  # Retornar None si no se encuentra la factura
        except Exception as e:
            app.logger.error(f"Error al obtener factura: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarFactura(self, descripcion):

        insertFacturaSQL = """
        INSERT INTO facturas(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertFacturaSQL, (descripcion,))
            factura_id = cur.fetchone()[0]
            con.commit()  # se confirma la insercion
            return factura_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar factura: {str(e)}")
            con.rollback()  # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateFactura(self, id, descripcion):

        updateFacturaSQL = """
        UPDATE facturas
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateFacturaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount  # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0  # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar factura: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteFactura(self, id):

        deleteFacturaSQL = """
        DELETE FROM facturas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteFacturaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar factura: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()
