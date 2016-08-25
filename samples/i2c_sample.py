from common.servoserver import ServoServer
import Adafruit_PCA9685

servomin = 150
servomax = 600

def value2pwm(v):
    v = 0 if v < 0 else v
    v = 255 if v > 255 else v
    return int(v / 255.0 * (servomax - servomin)) + servomin

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def callback(channels):
    pwm.set_pwm(0, 0, value2pwm(channels[0]))
    pwm.set_pwm(1, 0, value2pwm(channels[1]))

server = ServoServer(callback)
server.start()
