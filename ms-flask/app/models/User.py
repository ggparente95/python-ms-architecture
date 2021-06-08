import jwt
from app.database import db
from flask_bcrypt import Bcrypt
from app.config import SECRET_KEY


class User(db.Model):
    """ This class defines user model and its methods
    """

    __tablename__ = 'users'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    dni = db.Column(db.String(30), nullable=False, unique=True)
    admin = db.Column(db.Boolean(), default=False)

    # Foreign Key
    area_id = db.Column(db.ForeignKey('areas.id'),
                                nullable=False)


    def __init__(self, password, name, surname, email,
                dni, area_id, admin=False):
        """Create new user
        """
        self.name = name
        self.surname = surname
        self.email = email
        self.admin = admin
        self.password = Bcrypt().generate_password_hash(password).decode()
        self.dni = dni
        self.area_id = area_id

    def password_is_valid(self, password):
        """Check if password is valid, comparing it against the hashed.
        """
        return Bcrypt().check_password_hash(self.password, password)

    def generate_token(self):
        """Genera el token de acceso a partir del id de usuario
        """
        try:
            payload = {
                'iat': datetime.utcnow(),
                'id': self.id,
                'name': self.name,
                'surname': self.surname,
                'admin': self.admin,
                'email': self.email
                }

            # Create token using payload
            jwt_token = jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
            return jwt_token.decode("utf-8")

        except Exception as e:
            return str(e)

    def to_dict(self):
        """Convierte a un formato diccionario el usuario
        """
        d = {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'surname': self.surname,
            'dni': self.dni,
            'admin': self.admin,
            'area': self.get_area()
        }
        return d

    def get_area(self):
        """Returns user's area
        """
        return (None if not self.area else self.area.to_dict())

    def set_passowrd(self, password):
        """Set a new password"""
        if password:
            self.password = Bcrypt().generate_password_hash(password).decode()
