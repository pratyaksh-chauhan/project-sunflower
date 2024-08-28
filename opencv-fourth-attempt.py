import cv2
import numpy as np
from piservo import Servo
import time

verticalServo = Servo(12)
horizontalServo = Servo(13)

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Error Opening Video Stream Or File")

# lower = np.array([0, 0, 225])
# upper = np.array([201, 66, 255])

lower = np.array([15, 120, 20])
upper = np.array([35, 255, 255])

max_sweep_angle_horizontal = 120
max_sweep_angle_vertical = 60

while cap.isOpened():
    ret, frame = cap.read()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    img_height = frame.shape[0]
    img_width = frame.shape[1]

    sweep_rate_horizontal = max_sweep_angle_horizontal / img_width
    sweep_rate_vertical = max_sweep_angle_vertical / img_height

    offset_horizontal = 30
    offset_vertical = 20

    center_horizontal = None
    center_vertical = None

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if 0.7 < w/h < 1.3 and 500 < cv2.contourArea(contour):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                center_horizontal = x + (w / 2)
                center_vertical = y + (h / 2)

                calculated_sweep_angle_horizontal = center_horizontal * sweep_rate_horizontal + offset_horizontal
                calculated_sweep_angle_vertical = max_sweep_angle_vertical - center_vertical * sweep_rate_vertical + offset_vertical

                print("Calculated - " , calculated_sweep_angle_horizontal, ", ", calculated_sweep_angle_vertical)
                horizontalServo.write(calculated_sweep_angle_horizontal)
                verticalServo.write(calculated_sweep_angle_horizontal)

    if ret:
        cv2.imshow('frame', frame)
        cv2.imshow("mask", mask)
        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
