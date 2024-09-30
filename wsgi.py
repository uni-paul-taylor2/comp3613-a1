import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import *


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')
    print(create_competition('competition.json'))

'''
Competition Commands
'''

competition_cli = AppGroup('competition', help='Competition management commands')

@competition_cli.command('create')
@click.argument('filename', default='competition.json')
def create_competition(filename):
    try:
        print(create_competition(filename))
    except:
        print(f"Creating a competition from '{filename}' failed")

@competition_cli.command('scores')
@click.argument('competition_name', default='code4bread')
def competition_scores(competition_name):
    try:
        print(list_competitors(competition_name))
    except:
        print(f"Error listing scores of the competition: {competition_name}")

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User management commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    try:
        create_user(username, password)
        print(f'{username} created!')
    except:
        print(f"Failed to create user {username}")

# this command will be : flask user create bob bobpass

@user_cli.command('ranking')
@click.argument('username', default='rob')
@click.argument('competition_name', default='code4bread')
def user_ranking(username,competition_name):
    try:
        print(get_user_ranking(username,competition_name))
    except:
        print(f"Failed to get the ranking of '{username}' in the competition '{competition_name}'")

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)