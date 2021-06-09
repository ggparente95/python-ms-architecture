from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()
logger = logging.getLogger(__name__)


def obtener_todas_las_instancias(model):
    """Devuelve todas las instancias de un modelo
    """
    data = model.query.all()
    return data


def get_filtered_instances(model, **kwargs):
    """Devuelve todas las instancias segun el filtro aplicado en kwargs
    """
    instancias = model.query.filter_by(**kwargs).all()
    return instancias


def get_one_instance(model, **kwargs):
    """Devuelve la primer instancia filtrada segun la llave/valor
    del argumento
    """
    instancia = model.query.filter_by(**kwargs).first()
    return instancia


def get_one_instance_por_id(model, id):
    """Devuelve una instancia segun el id
    """
    return get_one_instance(model, id=id)

def add_instance(model, **kwargs):
    """Agrega una instancia con todos sus pares key=value de atributos.
       Retorna:
       - La instancia creada en caso de exito.
       - False en caso de excepcion.
    """
    try:
        instance = model(**kwargs)
        db.session.add(instance)
        commit_changes()
        return instance
    except Exception as e:
        logger.exception("Error agregando instancia\n {}".format(e))
        return False


def delete_instance(model, id):
    """Elimina una instancia por id
    """
    m = model.query.filter_by(id=id).first()
    try:
        db.session.delete(m)
        commit_changes()
        return True
    except Exception as e:
        logger.exception("Error eliminando una instancia\n{}".format(e))
        return False


def delete_instances_filtradas(model, **kwargs):
    """Elimina varias instancias por filtro
    """
    instancias = model.query.filter_by(**kwargs)
    todo_ok = True
    for i in instancias:
        try:
            db.session.delete(i)
            commit_changes()
        except Exception as e:
            logger.exception("Error eliminando una instancia\n{}".format(e))
            todo_ok = False

    return todo_ok


def update_instance(model, id, **kwargs):
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

    add_and_commit(instance)
    return todo_ok


def commit_changes():
    """Commitea los cambios
    """
    db.session.commit()


def add_and_commit(*args):
    """Recibe muchas instancias, la agregas a la base y commitea
    """
    for arg in args:
        db.session.add(arg)

    commit_changes()
