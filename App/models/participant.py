from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Participant(db.Model): #The bridge table
    __tablename__ = "Participant"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('Competition.id'), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    points = db.Column(db.Integer, default=0)
    time = db.Column(db.Integer, default=0)
    
    def __init__(self, user_id, points, time):
        self.user_id = user_id
        self.points = points
        self.time = time
        db.session.add(self)

    def __repr__(self):
        return f" <user:{self.user_id}, competition:{self.competition_id}, points:{self.points}, time:{self.time}> "
