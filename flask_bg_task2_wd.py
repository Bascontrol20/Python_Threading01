from flask import Flask
from time import sleep
from threading import Thread
from datetime import datetime
import pymcprotocol

app = Flask(__name__)


def background_task():
    while True:

        print(datetime.now())
        # Set frame type
        slmp = pymcprotocol.Type3E()
        # Set PLC type
        slmp = pymcprotocol.Type3E(plctype="iQ-R")
        # Connect PLC
        slmp.connect("192.168.1.81",8880)
        # SLMP batch bit read M8000#
        batch_read_val_bit = slmp.batchread_bitunits(headdevice="M8000", readsize=25)

        if batch_read_val_bit[0] == 1:
            print("M8000 On")

        if batch_read_val_bit[1] == 1:
            print("M8001 On")

        if batch_read_val_bit[2] == 1:
            print("M8002 On")
        
        if batch_read_val_bit[3] == 1:
            print("M8003 On")

        if batch_read_val_bit[4] == 1:
            print("M8004 On")

        sleep(1)


@app.route("/")
def hello_world():
    return "<p>Hello, Ram!</p>"


if __name__ == "__main__":
    thread = Thread(target=background_task)
    thread.daemon = True
    thread.start()
    app.run()
