from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.equipo.EquipoDao import EquipoDao

equapi = Blueprint('equapi', __name__)

# Trae todos los equipos
@equapi.route('/equipos', methods=['GET'])
def getEquipos():
    equdao = EquipoDao()

    try:
        equipos = equdao.getEquipos()  # Puedes cambiar el método si tienes uno específico para equipos

        return jsonify({
            'success': True,
            'data': equipos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los equipos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@equapi.route('/equipos/<int:equipo_id>', methods=['GET'])
def getEquipo(equipo_id):
    equdao = EquipoDao()

    try:
        equipo = equdao.getEquipoById(equipo_id)  # Cambia el método si tienes uno específico para equipos

        if equipo:
            return jsonify({
                'success': True,
                'data': equipo,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el equipo con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener equipo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo equipo
@equapi.route('/equipos', methods=['POST'])
def addEquipo():
    data = request.get_json()
    equdao = EquipoDao()

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
        equipo_id = equdao.guardarEquipo(descripcion)  # Cambia el método si tienes uno específico para equipos
        if equipo_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': equipo_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar el equipo. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar equipo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@equapi.route('/equipos/<int:equipo_id>', methods=['PUT'])
def updateEquipo(equipo_id):
    data = request.get_json()
    equdao = EquipoDao()

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
        if equdao.updateEquipo(equipo_id, descripcion.upper()):  # Cambia el método si tienes uno específico para equipos
            return jsonify({
                'success': True,
                'data': {'id': equipo_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el equipo con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar equipo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@equapi.route('/equipos/<int:equipo_id>', methods=['DELETE'])
def deleteEquipo(equipo_id):
    equdao = EquipoDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if equdao.deleteEquipo(equipo_id):  # Cambia el método si tienes uno específico para equipos
            return jsonify({
                'success': True,
                'mensaje': f'Equipo con ID {equipo_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el equipo con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar equipo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
