from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.factura.FacturaDao import FacturaDao

facapi = Blueprint('facapi', __name__)

# Trae todas las facturas
@facapi.route('/facturas', methods=['GET'])
def getFacturas():
    facdao = FacturaDao()

    try:
        facturas = facdao.getFacturas()

        return jsonify({
            'success': True,
            'data': facturas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las facturas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@facapi.route('/facturas/<int:factura_id>', methods=['GET'])
def getFactura(factura_id):
    facdao = FacturaDao()

    try:
        factura = facdao.getFacturaById(factura_id)

        if factura:
            return jsonify({
                'success': True,
                'data': factura,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la factura con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener factura: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva factura
@facapi.route('/facturas', methods=['POST'])
def addFactura():
    data = request.get_json()
    facdao = FacturaDao()

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
        factura_id = facdao.guardarFactura(descripcion)
        if factura_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': factura_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar la factura. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar factura: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@facapi.route('/facturas/<int:factura_id>', methods=['PUT'])
def updateFactura(factura_id):
    data = request.get_json()
    facdao = FacturaDao()

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
        if facdao.updateFactura(factura_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': factura_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la factura con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar factura: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@facapi.route('/facturas/<int:factura_id>', methods=['DELETE'])
def deleteFactura(factura_id):
    facdao = FacturaDao()

    try:
        # Usar el retorno de eliminarFactura para determinar el éxito
        if facdao.deleteFactura(factura_id):
            return jsonify({
                'success': True,
                'mensaje': f'Factura con ID {factura_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la factura con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar factura: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
