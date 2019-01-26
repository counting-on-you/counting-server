import threading
import sys
import time
import json

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def return_data():
    
        
    test_data = [
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

    string_data = json.dumps(test_data)

    print(string_data)

    sys.stdout.flush()

# Outputs new data every 5 minutes
while True:
    return_data()
    time.sleep(300)
