
import time, datetime, bluetooth as bt
from bluetooth import BluetoothSocket
import csv
DEBUG=0

print("Search nearby devices...")
# Search devices
nearby_devices = bt.discover_devices(lookup_names=True)
print( "found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
     print("addr {} name {}".format(addr,name))

# list of tuples nearby_devices = [("a","b")("c","d")]
# convert to dict with key:value -> name:addr
nearby_devices = dict((name,addr) for addr,name in nearby_devices)

if DEBUG: print(nearby_devices)

# Create the client socket
btsocket = BluetoothSocket(bt.RFCOMM)

try:
    hc05 = nearby_devices.get("\r\n")
    print(" Try connect to MAC ",hc05)
    btsocket.connect((hc05, 1))
    pass
except bt.btcommon.BluetoothError as error:
    print(" BluetoothError:", error)
    btsocket.close()
    pass
print(" connected!");

while(1):
    # Request data every 5 seconds
    time.sleep(10)
    # Open file in mode 'a' append data
    now = datetime.datetime.now()

    filename=now.strftime("%d-%m-%y")+"_log.txt"

    csvfile = open(filename, 'a')

    print("Resquesting log")
    # Send Listening flag 'L'
    btsocket.send("L")
    end=False;
    while(not end):
   #Receive data
         msg = btsocket.recv(1024)
         # Check if is End flag 'E'
         if b'E' in msg:
            msg = msg.strip(b'E')
            end=True
         writer = csvfile.write(msg.decode('utf-8')) 
