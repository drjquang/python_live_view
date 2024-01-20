# Date: Sat, 19-Jan-2024
# Desc: Center, generates winning number
# Info: Write to realtime database RLG3
#       Not yet construct timestamp from unique string id

import firebase_admin
from firebase_admin import credentials, db, firestore
import threading
import time
import random
import datetime

COUNTDOWN_SEC = 10


def generate_winning_number():
    random_number = random.randint(0, 36)
    return random_number


def countdown_timer():
    seconds = COUNTDOWN_SEC
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("-------- Generate winning number ----------")
    # When one minutes is finished, do the task
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
    database.child('RLG3/number_of_game').set(game_no+1)


def timer_thread():
    while True:
        countdown_timer()


timer_thread = threading.Thread(target=timer_thread)
cred = credentials.Certificate('servicesAccountKey.json')
# database = db.reference()

try:
    # Initialize the Firebase app
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://chatapp-80eeb-default-rtdb.firebaseio.com'
    })

    print("Successfully connected to Firebase!")

    # Get a reference to the database service
    database = db.reference()

    # Your database operations go here
    # Example: Write data to the database
    # data = {
    #     'message': 'Good morning, Firebase!'
    # }
    #
    # database.child('example').set(data)
    #
    # # Example: Read data from the database
    # result = database.child('example').get()
    # print(result['message'])
    # ----------------------------------------------------------------------------------------------

    # Start the timer thread only connecting to firebase successfully
    timer_thread.start()
    # Wait for the timer thread to finish
    timer_thread.join()

except Exception as e:
    print(f"Failed to connect to Firebase. Error: {e}")
