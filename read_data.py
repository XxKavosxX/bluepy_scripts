import bluepy.btle as btle
 
class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        print(data.decode("utf-8"))
 
p = btle.Peripheral("9C:1D:58:8A:A5:87")
p.withDelegate(ReadDelegate())
 
while True:
    while p.waitForNotifications(1):
        pass
 
p.disconnect()
