from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.cliente.ClienteDao import ClienteDao

sucapi = Blueprint('sucapi', __name__)

# Trae todas las sucursales
@sucapi.route('/sucursales', methods=['GET'])
def getSucursales():
    sucdao = ClienteDao()

    try:
        sucursales = sucdao.getClientes()  # Puedes mantener el método como está si devuelve las sucursales

        return jsonify({
            'success': True,
            'data': sucursales,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las sucursales: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sucapi.route('/sucursales/<int:sucursal_id>', methods=['GET'])
def getSucursal(sucursal_id):
    sucdao = ClienteDao()

    try:
        sucursal = sucdao.getClienteById(sucursal_id)  # Método para obtener una sucursal por ID

        if sucursal:
            return jsonify({
                'success': True,
                'data': sucursal,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la sucursal con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener sucursal: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva sucursal
@sucapi.route('/sucursales', methods=['POST'])
def addSucursal():
    data = request.get_json()
    sucursal = ClienteDao()

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
        sucursal_id = sucursal.guardarCliente(descripcion)  # Método para guardar la sucursal
        if sucursal_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': sucursal_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar la sucursal. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar sucursal: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sucapi.route('/sucursal/<int:sucursal_id>', methods=['PUT'])
def updateSucursal(sucursal_id):
    data = request.get_json()
    sucdao = ClienteDao()

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
        if sucdao.updateCliente(sucursal_id, descripcion.upper()):  # Método para actualizar la sucursal
            return jsonify({
                'success': True,
                'data': {'id': sucursal_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la sucursal con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar sucursal: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sucapi.route('/sucursales/<int:sucursal_id>', methods=['DELETE'])
def deleteSucursal(sucursal_id):
    sucdao = ClienteDao()

    try:
        # Usar el retorno de eliminarSucursal para determinar el éxito
        if sucdao.deleteCliente(sucursal_id):  # Método para eliminar la sucursal
            return jsonify({
                'success': True,
                'mensaje': f'Sucursal con ID {sucursal_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la sucursal con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar sucursal: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
