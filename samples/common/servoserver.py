from rsserver import RemoteSensorServer

class ServoServer(RemoteSensorServer):
    def __init__(self, callback=None):
        RemoteSensorServer.__init__(self)
        self.callback = callback
        self.channels = [0]*30
        self.channel2index = {}
        for i in range(1,31):
            ch = 'ch'+str(i)
            self.channel2index[ch] = i-1

    def sensorUpdate(self, dic):
        for key in dic:
            if key in self.channel2index:
                index = self.channel2index[key]
                self.channels[index] = dic[key]
#                print key, index, dic[key]

    def broadcast(self, message):
        if message == 'servo changed':
            if self.callback != None:
                self.callback(self.channels)

def callback(arr):
    print arr
                
if __name__ == "__main__":
    server = ServoServer(callback)
    server.start()
