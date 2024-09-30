from App.models import User, Competition, Participant
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    
def get_user_ranking(username,competition_name):
    user = get_user_by_username(username)
    competition = Competition.query.filter_by(name=competition_name).first()
    participants = Participant.query.order_by(
        Participant.points.desc(),
        Participant.time.asc()
    ).filter_by(competition_id=competition.id)
    i = -1
    for participant in participants:
        i += 1
        if participant.user_id == user.id:
            return i
    return i
    