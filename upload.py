import sys
import pyrebase
import os
import settings
import time
import json

print('Initializing program')

API_KEY = os.getenv('API_KEY')
AUTH_DOMAIN = os.getenv('AUTH_DOMAIN')
DATABASE_URL = os.getenv('DATABASE_URL')
STORAGE_BUCKET = os.getenv('STORAGE_BUCKET')
DEVICE_ID = os.getenv('DEVICE_ID')

config = {
  'apiKey': API_KEY,
  'authDomain': AUTH_DOMAIN,
  'databaseURL': DATABASE_URL,
  'storageBucket': STORAGE_BUCKET
}

def read_data(variable):
    print('Called read_data with variable: {}'.format(variable))
    # Get a reference to the database service
    print("Device ID: {}".format(DEVICE_ID))

    db = firebase.database()

    if variable is None or variable == "":
        print("Data was none")
        return

    # data to save

    try:
        data = json.loads(variable)
    except:
        return

    '''
    SAMPLE DATA

    [
        {
            "rssi": -86.0,
            "mac": "90:e7:c4:xx:xx:xx",
            "company": "HTC Corporation"
        },
        {
            "rssi": -84.0,
            "mac": "80:e6:50:xx:xx:xx",
            "company": "Apple, Inc."
        },
        {
            "rssi": -49.0,
            "mac": "ac:37:43:xx:xx:xx",
            "company": "HTC Corporation"
        }
    ]
    '''

    now = int(time.time())
    print(now)
    # Pass the user's idToken to the push method
    results = db.child("data").child(DEVICE_ID).child(now).set(data)


firebase = pyrebase.initialize_app(config)
if firebase is None:
    print('Error initializing firebase')
    exit(0)
else:
    print('Firebase up and running')

# First read data from command line
while True:
    data = sys.stdin.readline()
    print(data)
    if data:
        read_data(data)
    else:
        continue

print("Progam terminated")