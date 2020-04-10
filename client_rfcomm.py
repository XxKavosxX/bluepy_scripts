
from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("20:14:04:16:39:44", 1))

client_socket.send("Hello World")

print("Finished")

client_socket.close()
