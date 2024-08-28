from piservo import Servo
import time
# upper chine
myservo = Servo(12)
# dae bae
# myservo2 = Servo(13)

angle = 90
direction = 1

# angle2 = 90
# direction2 = 1


while 1 :
    # myservo.write(120)
    # time.sleep(1)

    myservo.write(angle)
    time.sleep(0.01)
    if direction == 1:
        angle = angle - .1
    else:
        angle = angle + .1
    
    if angle > 110 or angle < 20:
        direction = direction * -1

    # Second Servo logic
    # myservo.write(90)
    # myservo2.write(90)
    # time.sleep(1)
    # myservo.write(80)
    # # time.sleep(1)
    # # Servo.stop()
    # myservo2.write(angle2)

    # if direction2 == 1:
    #     angle2 = angle2 + .2
    # else:
    #     angle2 = angle2 - .2 

    # if angle2 > 140 or angle2 < 1:
    #     direction2 = direction2 * -1

