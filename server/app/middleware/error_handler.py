from flask import jsonify


def register_error_handlers(app):

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "status": "error",
            "message": "Resource not found"
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500

    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500