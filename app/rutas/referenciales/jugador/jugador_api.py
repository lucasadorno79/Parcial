from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.jugador.JugadorDao import JugadorDao

jugapi = Blueprint('jugapi', __name__)

# Trae todos los jugadores
@jugapi.route('/jugadores', methods=['GET'])
def getJugadores():
    jugdao = JugadorDao()

    try:
        jugadores = jugdao.getJugadores()

        return jsonify({
            'success': True,
            'data': jugadores,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los jugadores: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@jugapi.route('/jugadores/<int:jugador_id>', methods=['GET'])
def getJugador(jugador_id):
    jugdao = JugadorDao()

    try:
        jugador = jugdao.getJugadorById(jugador_id)

        if jugador:
            return jsonify({
                'success': True,
                'data': jugador,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el jugador con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener jugador: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo jugador
@jugapi.route('/jugadores', methods=['POST'])
def addJugador():
    data = request.get_json()
    jugdao = JugadorDao()

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
        jugador_id = jugdao.guardarJugador(descripcion)
        if jugador_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': jugador_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar el jugador. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar jugador: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@jugapi.route('/jugadores/<int:jugador_id>', methods=['PUT'])
def updateJugador(jugador_id):
    data = request.get_json()
    jugdao = JugadorDao()

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
        if jugdao.updateJugador(jugador_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': jugador_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el jugador con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar jugador: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@jugapi.route('/jugadores/<int:jugador_id>', methods=['DELETE'])
def deleteJugador(jugador_id):
    jugdao = JugadorDao()

    try:
        if jugdao.deleteJugador(jugador_id):
            return jsonify({
                'success': True,
                'mensaje': f'Jugador con ID {jugador_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el jugador con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar jugador: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500