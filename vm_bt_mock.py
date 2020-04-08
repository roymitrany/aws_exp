import time

class Bluetoothctl:
    """A mock class that returns made up BT devices"""

    def __init__(self):
        self.available_devices = [{"mac_address":"11:11:11:11:11:11","name":"Ahmad  iPhone"},
								{"mac_address":"11:11:11:11:11:12","name":"Sasha Samsung"},
         							{"mac_address":"11:11:11:11:11:13","name":"Yossi Xiaomi"}]
 

    def get_available_devices(self):
        """Return a list of tuples of paired and discoverable devices."""
        return self.available_devices

    def start_scan(self):
        """Do nothing, just pretend"""
        print ("I am scamming!!!")
        time.sleep(1)

if __name__ == "__main__":

    print("Init bluetooth...")
    bl = Bluetoothctl()
    print("Ready!")
    bl.start_scan()
    print("Scanning for 10 seconds...")
    for i in range(0, 10):
        print(i)
        time.sleep(1)

    print(bl.get_discoverable_devices())
