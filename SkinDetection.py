import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
framewidth = 640
frameheight = 480
capbrightness = 130
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,capbrightness)

#creating trackbar to detect skin color

def empty(a):
    pass

cv2.namedWindow('skincolor')
cv2.resizeWindow('skincolor',640,240)
cv2.createTrackbar('Hue Min','skincolor',0,179,empty)
cv2.createTrackbar('Hue Max','skincolor',179,179,empty)
cv2.createTrackbar('Sat Min','skincolor',0,255,empty)
cv2.createTrackbar('Sat Max','skincolor',255,255,empty)
cv2.createTrackbar('Val Min','skincolor',0,255,empty)
cv2.createTrackbar('Val Max','skincolor',255,255,empty)



while (cap.isOpened()):

    ret, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos('Hue Min','skincolor')
    h_max = cv2.getTrackbarPos('Hue Max','skincolor')
    s_min = cv2.getTrackbarPos('Sat Min','skincolor')
    s_max = cv2.getTrackbarPos('Sat Max','skincolor')
    v_min = cv2.getTrackbarPos('Val Min','skincolor')
    v_max = cv2.getTrackbarPos('Val Max','skincolor')

    min_HSV = np.array([h_min, s_min, v_min], dtype = "uint8")
    max_HSV = np.array([h_max, s_max, v_max], dtype = "uint8")
    
    skinRegionHSV = cv2.inRange(imgHSV, min_HSV, max_HSV)
    skinHSV = cv2.bitwise_and(img, img, mask = skinRegionHSV)
    if ret == True:
         cv2.imshow('webCam',skinHSV)
         if cv2.waitKey(1) & 0xFF == ord('q'):
             break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()