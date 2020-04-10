import serial
import time
#os.system('rfcomm connect hci0 20:14:04:16:39:44')
ser = serial.Serial(port = "/dev/rfcomm0", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
# Wait to read from Arduino
print("Running script")
while 1:
    try:
        time.sleep(10)
        ser.write("R")
        myData = ser.readline()
        print(myData)
    except KeyboardInterrupt:
        ser.close()
        exit()
