import threading
import sys
import time
import json
import random


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def return_data():

    test_data = [{
        "rssi": -86.0,
        "mac": "90:e7:c4:xx:xx:xx",
        "company": "HTC Corporation"
    } for i in range(random.randint(5, 100))]
    string_data = json.dumps(test_data)

    print(string_data)

    sys.stdout.flush()


# Outputs new data every 5 minutes
while True:
    return_data()
    time.sleep(300)
