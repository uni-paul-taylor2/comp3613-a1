from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import json

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    points = db.Column(db.Integer, default=0)
    participation = db.relationship('Participant', backref='User')
    

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def __repr__(self):
        return json.dumps({
            'id': self.id,
            'username': self.username
        })

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)