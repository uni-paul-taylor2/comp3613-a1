from App.models import Competition
from App.database import db
import json

def create_competition(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    competition = Competition(data['name'],data['start'],data['stop'])
    db.session.commit()
    for item in data['participation']:
        competition.add_user(item['id'],item['points'],item['time'])
    db.session.commit()
    return f"Competition '{data['name']}' added successfully"
        

def list_competitors(competition_name):
    competition = Competition.query.filter_by(name=competition_name).first()
    participants = competition.participants
    return participants