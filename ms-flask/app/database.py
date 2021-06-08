from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()
logger = logging.getLogger(__name__)


def obtener_todas_las_instancias(model):
    """Devuelve todas las instancias de un modelo
    """
    data = model.query.all()
    return data


def obtener_instancias_filtradas(model, **kwargs):
    """Devuelve todas las instancias segun el filtro aplicado en kwargs
    """
    instancias = model.query.filter_by(**kwargs).all()
    return instancias


def obtener_una_instancia(model, **kwargs):
    """Devuelve la primer instancia filtrada segun la llave/valor
    del argumento
    """
    instancia = model.query.filter_by(**kwargs).first()
    return instancia


def obtener_una_instancia_por_id(model, id):
    """Devuelve una instancia segun el id
    """
    return obtener_una_instancia(model, id=id)

def agregar_instancia(model, **kwargs):
    """Agrega una instancia con todos sus pares key=value de atributos.
       Retorna:
       - La instancia creada en caso de exito.
       - False en caso de excepcion.
    """
    try:
        instance = model(**kwargs)
        db.session.add(instance)
        commitear_cambios()
        return instance
    except Exception as e:
        logger.exception("Error agregando instancia\n {}".format(e))
        return False


def eliminar_instancia(model, id):
    """Elimina una instancia por id
    """
    m = model.query.filter_by(id=id).first()
    try:
        db.session.delete(m)
        commitear_cambios()
        return True
    except Exception as e:
        logger.exception("Error eliminando una instancia\n{}".format(e))
        return False


def eliminar_instancias_filtradas(model, **kwargs):
    """Elimina varias instancias por filtro
    """
    instancias = model.query.filter_by(**kwargs)
    todo_ok = True
    for i in instancias:
        try:
            db.session.delete(i)
            commitear_cambios()
        except Exception as e:
            logger.exception("Error eliminando una instancia\n{}".format(e))
            todo_ok = False

    return todo_ok


def editar_instancia(model, id, **kwargs):
    """Edita los pares key=value de atributos recibidos de una instancia.
    Si el value es None no actualiza.
    """
    todo_ok = True
    instance = model.query.filter_by(id=id).all()[0]

    for attr, new_value in kwargs.items():
        if ((type(new_value) == bool) or new_value is None):
            try:
                setattr(instance, attr, new_value)
            except Exception as e:
                logger.exception("Error editando una instancia\n{}".format(e))
                todo_ok = False
        else:
            if new_value or ((type(new_value) == int) and new_value == 0):
                try:
                    setattr(instance, attr, new_value)
                except Exception as e:
                    logger.exception("Error editando"
                                     " una instancia\n{}".format(e))
                    todo_ok = False

    agregar_y_commitear(instance)
    return todo_ok


def commitear_cambios():
    """Commitea los cambios
    """
    db.session.commit()


def agregar_y_commitear(*args):
    """Recibe muchas instancias, la agregas a la base y commitea
    """
    for arg in args:
        db.session.add(arg)

    commitear_cambios()
