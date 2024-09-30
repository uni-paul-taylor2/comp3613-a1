from App.models import Competition
from App.database import db
import json
from functools import cmp_to_key

def create_competition(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    competition = Competition(data['name'],data['start'],data['stop'])
    db.session.commit()
    for item in data['participation']:
        competition.add_user(item['id'],item['points'],item['time'])
    db.session.commit()
    return f"Competition '{data['name']}' added successfully"
        
def participant_comparator(participant1, participant2):
    if participant1.points > participant2.points:
        return -1
    elif participant1.points < participant2.points:
        return 1
    else:
        if participant1.time < participant2.time:
            return -1
        elif participant1.time > participant2.time:
            return 1
        else:
            return 0

def list_competitors(competition_name):
    competition = Competition.query.filter_by(name=competition_name).first()
    participants = competition.participants
    return sorted(participants, key=cmp_to_key(participant_comparator))