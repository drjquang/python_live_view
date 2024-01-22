# Date: Mon, 21-Jan-2024
# Desc: This will count how many nodes in the longmeter

import firebase_admin
from firebase_admin import credentials, db

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

    # Do something in the middle
    target_path = database.child('RLG3').child('longmeter')
    data = target_path.get()
    if data:
        number_of_nodes = len(data)
    else:
        print("No data found in the database.")

    # Terminate the connection
    firebase_admin.delete_app(firebase_admin.get_app())

    # Announcement
    print("Number of nodes in longmeter {}.".format(number_of_nodes))

except Exception as e:
    print(f"Failed to connect to Firebase. Error: {e}")
