from flask import jsonify


def error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'message': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({'message': 'Internal server error'}), 500
