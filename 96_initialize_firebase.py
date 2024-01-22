# Date: Mon, 21-Jan-2024
# Desc: This will initialize the Firebase realtime database, path RLG3
# Info: number_of_sample = 200

import random
import firebase_admin
from firebase_admin import credentials, db


def generate_winning_number():
    random_number = random.randint(0, 36)
    return random_number


def write_one_number():
    winning_number = generate_winning_number()
    get_number = database.child('RLG3').get()
    game_no = get_number['number_of_game']
    constructed_data = {
        'game_no': game_no,
        'winning_number': winning_number
    }
    new_node_ref = database.child('RLG3/longmeter').push(constructed_data)
    constructed_data.update({'node_name': new_node_ref.key})
    database.child('RLG3/current').set(constructed_data)
    database.child('RLG3/number_of_game').set(game_no + 1)


number_of_sample = 200
# Read the current to retrieve uid
cred = credentials.Certificate('servicesAccountKey.json')

try:
    # Initialize the Firebase app (start the connection)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://chatapp-80eeb-default-rtdb.firebaseio.com'
    })
    print("Successfully connected to Firebase!")

    # Get a reference to the database service
    database = db.reference()

    # Repeat times
    for i in range(number_of_sample):
        write_one_number()

    # Terminate the connection
    firebase_admin.delete_app(firebase_admin.get_app())

    # Announcement
    print("Generating {} samples.".format(number_of_sample))

except Exception as e:
    print(f"Failed to connect to Firebase. Error: {e}")
