from app.database import add_instance, update_instance, \
                         delete_instance, get_one_instance, \
                         get_filtered_instances, \
                         obtener_todas_las_instancias
from app.models.User import User
from app.models.Area import Area


def get_users():
    '''Returns all the users
    '''
    instances = obtener_todas_las_instancias(User)
    formatted_instances = [i.to_dict() for i in instances]
    return formatted_instances


def get_filtered_users(**args):
    '''Returns all the users filtering
    '''
    instances = get_filtered_instances(User, **args)
    if len(instances) == 1:
        return instances[0].to_dict()
    else:
        formatted_instances = [i.to_dict() for i in instances]
        return formatted_instances


def create_user(data):
    '''Creates a user
    '''
    try:
        user = add_instance(User, **data)
    except Exception as e:
        print(e)
        return None, "An unexpected error ocurred"
    return user, None


def delete_user(id):
    '''Delete a user
    '''
    try:
        delete_instance(User, id=id)
    except Exception as e:
        print(e)
        return False, "An unexpected error ocurred"
    return True, ""


def update_user(id, data):
    '''Update user info
    '''
    update_instance(User, id=id, **data)
    return True, ""


def populate_areas():
    '''Populate areas table
    '''
    areas = get_one_instance(Area, name="Gerencia")
    if not areas:
        add_instance(Area, name="Gerencia")

def populate_users():
    '''Populate users table
    '''
    user = get_one_instance(User, email="admin@admin.com")
    if user:
        return
    add_instance(User, email="admin@admin.com", name="Gaston",
                      surname="Parente", dni="32123", password="admin123",
                      area_id=1, admin=True)
    add_instance(User, email="admin2@admin.com", name="Jorge",
                      surname="Perez", dni="321233", password="admin123",
                      area_id=1, admin=True)
