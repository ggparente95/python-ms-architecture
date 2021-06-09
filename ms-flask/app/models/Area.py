from app.database import db


class Area(db.Model):
    """This class define areas of the company
    """
    __tablename__ = 'areas'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Enum('Management', 'Sales', 'Gerencia',
                             name='myenum'), unique=True)

    users = db.relationship('User',
                            backref='area',
                            cascade="save-update, merge, "
                                    "delete, delete-orphan")

    def to_dict(self):
        d = {
            'id': self.id,
            'name': self.name
        }
        return d