from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models import Participant, User

class Competition(db.Model):
    __tablename__ = "Competition"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    start_time = db.Column(db.Integer, nullable=False)
    stop_time = db.Column(db.Integer, nullable=False)
    participants = db.relationship('Participant', backref='Competition')
    
    def __init__(self, name, start, stop):
        self.name = name
        self.start_time = start
        self.stop_time = stop
        db.session.add(self)

    def __repr__(self):
        return self.name

    def add_user(self, id, points, time):
        user = User.query.get(id)
        user.points += points
        Participant(user.id,self.id,points,time) #classes when initialised add themselves to the session
        db.session.add(user) #add to session after edit
