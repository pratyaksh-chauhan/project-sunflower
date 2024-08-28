import cv2
import numpy as np
from piservo import Servo
import time

myservo = Servo(12)

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Error Opening Video Stream Or File")

lower = np.array([0, 0, 225])
upper = np.array([201, 66, 255])

# 960 540

while cap.isOpened():
    ret, frame = cap.read()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    height = frame.shape[0]
    width = frame.shape[1]

    angle_per_pixel = 90/width

    # modified_frame = cv2.resize(frame, (new_width, new_height))
    # modified_mask = cv2.resize(mask, (new_width, new_height))

    img_center_x = None
    img_center_y = None

    screen_center_x = width / 2
    screen_center_y = height / 2

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 1000 and cv2.contourArea(contour) < 6000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                img_center_x = x + (w / 2)
                img_center_y = y + (h / 2)

                # diff_x = screen_center_x - img_center_x
                # diff_y = screen_center_y - img_center_y

                # print(diff_x, ", ", diff_y)
                print(img_center_x * angle_per_pixel)
                # myservo.write(img_center_x * angle_per_pixel)
                # time.sleep(3)
                # myservo.write(0)
                # time.sleep(3)
                # myservo.write(90)
                # time.sleep(3)
                
    # print(img_center_x, ", " , img_center_y, ", " , screen_center_x, ", " , screen_center_y)
    # print(center_x, ", " , center_y)

    if ret == True:
        cv2.imshow('frame', frame)
        cv2.imshow("mask", mask)
        # cv2.imshow("mask1", mask)
        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
