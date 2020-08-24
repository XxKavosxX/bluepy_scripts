#All you need https://ianharvey.github.io/bluepy-doc/
import datetime
import bluepy.btle as btle

class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):

        print("Data received")

        #Get currente datetime
        now = datetime.datetime.now()

        #Is file exist, open it, create if not
        filename = now.strftime("%m-%y")+"_log.txt"

        #Open file in append+binary mode
        file = open(filename, 'ab')

        #Decide data
        decoded = data.decode('utf-8')

        #Write data with format a0,b0,...z0;a1,b1,..,z1;a2,b2,..,z2
        writer = file.write(decoded+';')

BLELADDR = "D4:36:39:67:7F:2A"
p = btle.Peripheral(BLELADDR)
p.withDelegate(ReadDelegate())

#Infinity loop
while True:
    #Notification will be handled ever Data received
    while p.waitForNotifications(1):
        pass

#Disconnect
p.disconnect()
