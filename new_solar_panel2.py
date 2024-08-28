from piservo import Servo
import time

myservo = Servo(12)
myservo2 = Servo(13)

angle = 90
direction = 1


while 1 :
    myservo.write(angle)
    myservo2.write(angle)
    time.sleep(0.01)
    if direction == 1:
        angle = angle - .2
    else:
        angle = angle + .2
    
    if angle > 140 or angle < 30:
        direction = direction * -1
