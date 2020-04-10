import bluepy.btle as btle
 
class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        print(data.decode("utf-8"))
 
p = btle.Peripheral("20:14:04:16:39:44")
p.withDelegate(ReadDelegate())
 
while True:
    while p.waitForNotifications(1):
        pass
 
p.disconnect()
