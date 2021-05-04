from app.builder import ApiBuilder
from app.config import ConfigDev
from flask.cli import FlaskGroup


app_handler = ApiBuilder(ConfigDev)
app = app_handler.crear_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    """Crea la base de datos con todos sus modelos
    """
    app_handler.iniciar_db()
    app_handler.poblar_db()


if __name__ == '__main__':
    cli()
