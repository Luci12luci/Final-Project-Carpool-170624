from app import db
class User(db.Model):
    __tablename__ = "user"

    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)