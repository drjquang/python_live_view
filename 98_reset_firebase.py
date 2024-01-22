# Date: Mon, 21-Jan-2024
# Desc: This will reset the Firebase realtime database, path RLG3
# Info: Set number_of_game = 1
#       Delete (node) current and longmeter

import firebase_admin
from firebase_admin import credentials, db

initial_game_no = 1
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

    # Set the number_of_game = 1
    database.child('RLG3').child('number_of_game').set(initial_game_no)
    database.child('RLG3').child('current').delete()
    database.child('RLG3').child('longmeter').delete()

    # Terminate the connection
    firebase_admin.delete_app(firebase_admin.get_app())

    # Announcement
    print("Initializing firebase, set game_no = " + str(initial_game_no))
    print("Initializing firebase, delete current and longmeter")

except Exception as e:
    print(f"Failed to connect to Firebase. Error: {e}")
