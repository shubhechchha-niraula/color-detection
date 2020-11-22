import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red Color
    low_red = np.array([160, 155, 85])
    high_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask = red_mask)

    # Green Color
    low_green = np.array([45, 50, 70])
    high_green = np.array([75, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask = green_mask)

    # Blue Color
    low_blue = np.array([85, 80, 25])
    high_blue = np.array([125, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)

    # No white (Dark mode)
    low = np.array([0, 40, 0])
    high = np.array([180, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    dark = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Red_Frame", red)
    cv2.imshow("Green_Frame", green)
    cv2.imshow("Blue_Frame", blue)
    cv2.imshow("Dark_Frame", dark)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

