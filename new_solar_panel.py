from piservo import Servo
import time

myservo = Servo(12)

angle = 90
direction = 1

left_swipe_range=65
right_swipe_range=80

while 1 :
    myservo.write(angle)
    time.sleep(0.01)
    if direction == 1:
        angle = angle - .2
    else:
        angle = angle + .2
    
    if angle > (90+left_swipe_range/2) or angle < (90-right_swipe_range/2):
        direction = direction * -1
