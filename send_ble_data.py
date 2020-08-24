import bluepy.btle as btle
import time
 
p = btle.Peripheral("20:14:04:16:39:44")
#s = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
s = p.getServiceByUUID("00001101-0000-1000-8000-00805f9b34fb")
c = s.getCharacteristics()[0]
 
c.write("Hello World!\n")
p.disconnect()
