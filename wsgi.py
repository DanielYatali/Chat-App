import json
import click
from App.controllers.user_info import create_bot
# from App.controllers.user_info import create_bot, create_user_info

from App.database import create_db
from App.main import app, migrate
from App.controllers import ( create_user, get_all_users_json )


@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
@click.argument("email")
def create_user_command(username, email, password):
    create_user(username,email, password)
    print(f'{username} created!')

@app.cli.command("get-users")
def get_users():
    print(get_all_users_json())

@app.cli.command("create-bots")
def create_bots():
    with open('./dummy_data/bots.json') as json_file:
        bots = json.load(json_file)
        i = 0
        for bot in bots:
            print(create_user(bot["first_name"] + "_" + bot["last_name"]+ f"{i}", bot["email"], bot["first_name"]+"pass"))
            print(create_bot(bot))
            i += 1
    
        # # Print the type of data variable
        # print("Type:", type(bots))
    
        # # Print the data of dictionary
        # print("\nPeople1:", bots[0]['user_id'])
        # print("\nPeople2:", bots[0]['first_name'])