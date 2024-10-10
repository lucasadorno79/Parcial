from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.pago.PagoDao import PagoDao

pagapi = Blueprint('pagapi', __name__)

# Trae todos los pagos
@pagapi.route('/pagos', methods=['GET'])
def getPagos():
    pagdao = PagoDao()

    try:
        pagos = pagdao.getPagos()  # Cambia esto para que se refiera a pagos

        return jsonify({
            'success': True,
            'data': pagos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los pagos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pagapi.route('/pagos/<int:pag_id>', methods=['GET'])
def getPago(pag_id):
    pagdao = PagoDao()

    try:
        pago = pagdao.getPagoById(pag_id)  # Cambia esto para que se refiera a pagos

        if pago:
            return jsonify({
                'success': True,
                'data': pago,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el pago con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo pago
@pagapi.route('/pagos', methods=['POST'])
def addPago():
    data = request.get_json()
    pagdao = PagoDao()

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
        pag_id = pagdao.guardarPago(descripcion)  # Cambia esto para que se refiera a pagos
        if pag_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': pag_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el pago. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pagapi.route('/pagos/<int:pag_id>', methods=['PUT'])
def updatePago(pag_id):
    data = request.get_json()
    pagdao = PagoDao()

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
        if pagdao.updatePago(pag_id, descripcion.upper()):  # Cambia esto para que se refiera a pagos
            return jsonify({
                'success': True,
                'data': {'id': pag_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el pago con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pagapi.route('/pagos/<int:pag_id>', methods=['DELETE'])
def deletePago(pag_id):
    pagdao = PagoDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if pagdao.deletePago(pag_id):  # Cambia esto para que se refiera a pagos
            return jsonify({
                'success': True,
                'mensaje': f'Pago con ID {pag_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el pago con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
