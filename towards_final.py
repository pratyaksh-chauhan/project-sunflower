from piservo import Servo
import time

myservo = Servo(12)
myservo2 = Servo(13)

angle = 90
direction = 1

angle2 = 90
direction2 = 1


while 1 :
    # myservo2.write(90)
    # time.sleep(3)
    
    myservo.write(angle)
    time.sleep(0.01)
    if direction == 1:
        angle = angle - .05
    else:
        angle = angle + .05
    
    if angle > 120 or angle < 1:
        direction = direction * -1

    # Second Servo logic
    myservo2.write(angle2)
    if direction2 == 1:
        angle2 = angle2 + .01
    else:
        angle2 = angle2 - .01

    if angle2 > 120 or angle2 < 60:
        direction2 = direction2 * -1

