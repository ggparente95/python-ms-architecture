from flask import Flask, jsonify
from app.controllers.users_controller import users
from flask_cors import CORS


class ApiBuilder():

    def __init__(self, cfg):
        self.cfg = cfg
        #self.__db = None

    def crear_app(self):
        """Crea la aplicación, prepara la configuración y registra
        extensiones"""
        app = Flask(__name__)
        app.config.from_object(self.cfg)
        self.registrar_extensiones(app)
        self.registrar_error_handlers(app)
        return app

    def registrar_extensiones(self, app):
        """Registrar extensiones como blueprints, database, JWT
        """
        CORS(app, support_credentials=True)
        app.register_blueprint(users)
        #db.init_app(app)
        #migrate = Migrate(app, db)
        #self.__db = db

    def iniciar_db(self):
        """Inicia la base de datos dropeando todo y creandola"""
        # ¡ OJO MAQUINA ! Desactivas este comentario y limpias la db
        # self.destruir_db()
        # self.__db.create_all()
        # self.__db.session.commit()
        # self.poblar_db()
        return

    def destruir_db(self):
        # self.__db.session.remove()
        # self.__db.drop_all()
        return

    def poblar_db(self):
        # poblar_users(self.__db)
        # poblar_operaciones(self.__db)
        # poblar_notificaciones(self.__db)
        return

    def get_db(self):
        return self.__db


    def registrar_error_handlers(self, app):
        import traceback

        @app.errorhandler(404)
        def error_404_handler(e):
            app.logger.error('Hay un 404 ' + traceback.format_exc())
            return jsonify({'Mensaje': 'Error 404'}), 404

        @app.errorhandler(500)
        def error_500_handler(e):
            app.logger.error('Error 500 ' + traceback.format_exc())
            return jsonify({'Mensaje': 'Error 500'}), 500

        @app.errorhandler(403)
        def error_403_handler(e):
            app.logger.error('Error 403 ' + traceback.format_exc())
            return jsonify({'Mensaje': 'Error 403'}), 403

        @app.errorhandler(410)
        def error_410_handler(e):
            app.logger.error('Error 410 ' + traceback.format_exc())
            return jsonify({'Mensaje': 'Error 410'}), 410


