import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
lower = np.array([0, 0, 225])
upper = np.array([172, 111, 255])
while cap.isOpened():
    ret, frame = cap.read()

    frame2 = frame.copy()

    image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(image, lower, upper)

    new_height = int(frame.shape[0]*0.5)
    new_width = int(frame.shape[1]*0.5)
    
    img_center_x = None
    img_center_y = None

    screen_center_x = new_width/2
    screen_center_y = new_height/2

    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            if cv.contourArea(contour) > 500:
                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                diff_x = screen_center_x - img_center_x
                diff_y = screen_center_y - img_center_y

    if ret == True:
        cv.imshow('frame', frame)
        cv.imshow('frame2', frame2)
        if cv.waitKey(25) == ord('q'):
            break
    else:
        break

cv.waitKey(0)
cv.destroyAllWindows()
