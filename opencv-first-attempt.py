import cv2
import numpy as np

cap = cv2.VideoCapture('VID_20240115_220601.mp4')

if cap.isOpened() == False:
    print("Error Opening Video Stream Or File")

lower = np.array([0, 0, 225])
upper = np.array([172, 111, 255])

# 960 540

while cap.isOpened():
    ret, frame = cap.read()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    new_height = int(frame.shape[0]*0.5)
    new_width = int(frame.shape[1]*0.5)

    modified_frame = cv2.resize(frame, (new_width, new_height))
    modified_mask = cv2.resize(mask, (new_width, new_height))

    img_center_x = None
    img_center_y = None

    screen_center_x = new_width/2
    screen_center_y = new_height/2

    contours, hierarchy = cv2.findContours(modified_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(modified_frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                img_center_x = x + (w/2)
                img_center_y = y + (h/2)


    diff_x = screen_center_x - img_center_x
    diff_y = screen_center_y - img_center_y

    print(diff_x, ", ", diff_y)

    # print(img_center_x, ", " , img_center_y, ", " , screen_center_x, ", " , screen_center_y)
    # print(center_x, ", " , center_y)

    if ret == True:
        cv2.imshow('frame', modified_frame)
        cv2.imshow("mask", modified_mask)
        # cv2.imshow("mask1", mask)
        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
