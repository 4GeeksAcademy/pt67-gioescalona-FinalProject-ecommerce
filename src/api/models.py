from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)



    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # No se serializa la contraseña por motivos de seguridad
        }

class Jeans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    talla = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Vaqueros {self.marca} {self.talla}>'

    def serialize(self):
        return {
            "id": self.id,
            "talla": self.talla,
            "color": self.color,
            "marca": self.marca,
            "user_id": self.user_id
        }

class Shirts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    talla = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Camisetas {self.marca} {self.talla}>'

    def serialize(self):
        return {
            "id": self.id,
            "talla": self.talla,
            "color": self.color,
            "marca": self.marca,
            "user_id": self.user_id
        }

class Shoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    talla = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Zapatos {self.marca} {self.talla}>'

    def serialize(self):
        return {
            "id": self.id,
            "talla": self.talla,
            "color": self.color,
            "marca": self.marca,
            "user_id": self.user_id
        }
