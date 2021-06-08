from app.database import agregar_instancia, editar_instancia, \
                         eliminar_instancia, obtener_una_instancia, \
                         obtener_instancias_filtradas, \
                         obtener_todas_las_instancias
from app.models.User import User
from app.models.Area import Area


def get_users():
    '''Returns all the users
    '''
    instances = obtener_todas_las_instancias(User)
    formatted_instances = [i.to_dict() for i in instances]
    return formatted_instances

def populate_areas():
    '''Populate areas table
    '''
    areas = obtener_una_instancia(Area, name="Gerencia")
    if not areas:
        agregar_instancia(Area, name="Gerencia")

def populate_users():
    '''Populate users table
    '''
    user = obtener_una_instancia(User, email="admin@admin.com")
    if user:
        return
    agregar_instancia(User, email="admin@admin.com", name="Gaston",
                      surname="Parente", dni="32123", password="admin123",
                      area_id=1, admin=True)
    agregar_instancia(User, email="admin2@admin.com", name="Jorge",
                      surname="Perez", dni="321233", password="admin123",
                      area_id=1, admin=True)
