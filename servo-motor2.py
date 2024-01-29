from piservo import Servo
import time

myservo = Servo(12)
myservo2 = Servo(13)


while 1 :
    myservo.write(90)
    time.sleep(1)
    