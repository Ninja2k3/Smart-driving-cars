import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

while True:

    _,frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90,60,0])
    upper_blue = np.array([121,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    cnts = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)


    for c in cnts:
        area = cv2.contourArea(c)
        if area > 500:

            cv2.drawContours(frame, [c],-1,(0,255,0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Centre", (cx-20, cy-20), font,0.5, (0,255,0), 1)

            cv2.imshow("frame",frame)

    print("area is ...", area)
    print("centroid is at...",cx,cy)

    k = cv2.waitKey(1000)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
