from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_user('john', 'johnpass')
    create_user('jane', 'janepass')
    create_user('robert', 'roberto')
    create_user('3x+1', '6^edfa9*G') #because why not LOL
