from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.datosjugador.DatosjugadorDao import DatosjugadorDao

datapi = Blueprint('datapi', __name__)

# Trae todos los datos de jugadores
@datapi.route('/datosjugador', methods=['GET'])
def getDatosjugador():
    datdao = DatosjugadorDao()

    try:
        datosjugador = datdao.getDatosjugador()  # Asumiendo que la función sigue siendo válida

        return jsonify({
            'success': True,
            'data': datosjugador,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los datos de jugadores: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@datapi.route('/datosjugadores/<int:datosjugador_id>', methods=['GET'])
def getDatosjugador(datosjugador_id):
    datdao = DatosjugadorDao()

    try:
        datosjugador = datdao.getDatosjugador(datosjugador_id)

        if datosjugador:
            return jsonify({
                'success': True,
                'data': datosjugador,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el dato del jugador con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener dato de jugador: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo dato de jugador
@datapi.route('/datosjugador', methods=['POST'])
def addDatosjugador():
    data = request.get_json()
    datdao = DatosjugadorDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        descripcion = data['descripcion'].upper()
        datosjugador_id = datdao.guardarDatosjugador(descripcion)  # Aquí debería ajustarse según tu lógica
        if datosjugador_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': datosjugador_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el dato del jugador. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar dato de jugador: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@datapi.route('/datosjugadores/<int:datosjugador_id>', methods=['PUT'])
def updateDatosjugador(datosjugador_id):
    data = request.get_json()
    datdao = DatosjugadorDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    descripcion = data['descripcion']
    try:
        if datdao.updateDatosjugador(datosjugador_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': datosjugador_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el dato del jugador con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar dato de jugador: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@datapi.route('/datosjugadores/<int:datosjugador_id>', methods=['DELETE'])
def deleteDatosjugador(datosjugador_id):
    datdao = DatosjugadorDao()

    try:
        # Usar el retorno de eliminarDatosJugador para determinar el éxito
        if datdao.deleteDatosjugador(datosjugador_id):  # Ajustar según tu lógica
            return jsonify({
                'success': True,
                'mensaje': f'Dato del jugador con ID {datosjugador_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el dato del jugador con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar dato de jugador: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
