from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# contain a name, a birthday, and a list of animals that they take care of.
class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Integer)

    animals = db.relationship("Animal", backref = 'zookeeper')

    def __repr__(self):
        return f'<Animal Zookeeper {self.name},{self.birthday}>'


# contain an environment (grass, sand, or water), an open_to_visitors boolean, and a list of animals
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship("Animal", backref = 'enclosure')

    def __repr__(self):
        return f'<Animal Enclosure {self.environment}, {self.open_to_visitors}>'


# contain a name, a species, a zookeeper, and an enclosure.
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    # zookeepers.id refers to table name ###
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    def __repr__(self):
        return f'<Animal {self.name}, {self.species}>'
