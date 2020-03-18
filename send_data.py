import bluepy.btle as btle
import time
 
p = btle.Peripheral("9C:1D:58:8A:A5:87")
s = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
c = s.getCharacteristics()[0]
 
c.write("Hello World!\n")
p.disconnect()
