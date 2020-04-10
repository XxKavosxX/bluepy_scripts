import time, bluetooth as bt
from bluetooth import *

ack_devices = ["20:14:04:16:39:44", "48:49:C7:EF:AC:76"]
print("Search nearby devices...")
# Search devices
nearby_devices = bt.discover_devices(lookup_names=True)
print( "Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print( "ADDR {}, NAME {}".format(addr, name))

# Create the client socket
client_socket = BluetoothSocket(RFCOMM)

print("Create connection...");
# Try to connect
try:
    print(" Try connect to MAC ",ack_devices[0])
    client_socket.connect((ack_devices[0], 1))
    pass
except bt.btcommon.BluetoothError as error:
    print(" BluetoothError:", error)
    client_socket.close()
    pass

print(" connected!");

while(1):
    time.sleep(1)
    msg=client_socket.recv(1024)
    print(msg.decode('utf-8'))
    print("\n")
   # try:
   #    print("Recv message");
   #    msg = client_socket.recv(1024);
       #msg = bytes(msg, 'utf-8')
       #print(msg)
   #    print("Received [%s]" %msg)
   #    pass 
   # except bt.btcommon.BluetoothError as error:
   #    print("Erro when listen")
   #    pass

#print("Finished")
client_socket.close()
