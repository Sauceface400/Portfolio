from portfolio import db

class credencials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"Credencials('{self.username}')"