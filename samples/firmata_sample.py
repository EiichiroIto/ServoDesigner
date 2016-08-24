from common.servoserver import ServoServer
from pyfirmata import Arduino, util

port='/dev/tty.usbmodem1411'
board = Arduino(port)
board.servo_config(9)
board.servo_config(10)

def callback(channels):
    board.digital[9].write(channels[0]/255.0*180)
    board.digital[10].write(channels[1]/255.0*180)

server = ServoServer(callback)
server.start()
