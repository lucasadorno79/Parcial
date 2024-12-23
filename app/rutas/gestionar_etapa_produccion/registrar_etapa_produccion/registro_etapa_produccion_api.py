from flask import Blueprint, request, jsonify, current_app as app
from app.dao.gestionar_etapa_produccion.registrar_etapa_produccion.RegistroepDao import RegistroepDao

repapi = Blueprint('repapi', __name__)

# Trae todas las productos
@repapi.route('/registroep', methods=['GET'])
def getRegistroep():
    repdao = RegistroepDao()

    try:
        registroep = repdao.getRegistroep()
        
        return jsonify({
            'success': True,
            'data': registroep,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los registros: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@repapi.route('/registroep/<int:registroep_id>', methods=['GET'])
def getRegistroep(registroep_id):
    repdao = RegistroepDao()

    try:
        registroep = repdao.getRegistroepById(registroep_id)
        
        if registroep:
            return jsonify({
                'success': True,
                'data': registroep,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el registro con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener registro: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva producto
@repapi.route('/registroep', methods=['POST'])
def addRegistroep():
    data = request.get_json()
    repdao = RegistroepDao()
    
    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'color', 'categoria']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(str(data[campo]).strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre = data['nombre'].upper()
        color = data['color'].upper()
        categoria = data['categoria']

        registroep_id = repdao.guardarRegistroep(nombre, color, categoria)
        if registroep_id is not None:
            return jsonify({
                'success': True,
                'data': {
                    'id': registroep_id,
                    'nombre': nombre,
                    'color': color,
                    'categoria': categoria
                    
                },
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar el registro. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar registro: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@repapi.route('/registroep/<int:registroep_id>', methods=['PUT'])
def updateRegistroep(registroep_id):
    data = request.get_json()
    repdao = RegistroepDao()
    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'color', 'categoria']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(str(data[campo]).strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} {data} es obligatorio y no puede estar vacío.'
                            }), 400

    nombre = data['nombre'].upper()
    color = data['color'].upper()
    categoria = data['categoria']

    try:
        if repdao.updateRegistroep(registroep_id, nombre, color, categoria):
            return jsonify({
                'success': True,
                'data': {
                    'id': registroep_id,
                    'nombre': nombre,
                    'color': color,
                    'categoria': categoria
                },
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el registro con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar registro: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@repapi.route('/registroep/<int:registroep_id>', methods=['DELETE'])
def deleteRegistroep(registroep_id):
    perdao = RegistroepDao()

    try:
        if perdao.deleteRegistroep(registroep_id):
            return jsonify({
                'success': True,
                'mensaje': f'Registroep con ID {registroep_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el registroep con el ID proporcionado o no se pudo eliminar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al eliminar registroep: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500