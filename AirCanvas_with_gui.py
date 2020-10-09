import tkinter as tk
from tkinter.ttk import *
import cv2
import numpy as np


r = tk.Tk()
r.title('Air Canvas')

label_for_aircanvas = tk.Label(r,text='AIR CANVAS',bg='yellow',fg='blue',width=40,height=3,pady=1,anchor='center')
label_for_aircanvas.grid(column=2,row=1)


def empty(w):
    pass

def openTrackbar(event):
    cv2.namedWindow('color')
    cv2.resizeWindow('color',640,130)
    cv2.createTrackbar('Blue','color',0,255,empty)
    cv2.createTrackbar('Green','color',0,255,empty)
    cv2.createTrackbar('Red','color',0,255,empty)
    
Trackbar = tk.Button(r,text='TrackBarColor')
Trackbar.bind('<Button-1>',openTrackbar)
Trackbar.grid(row=4,columnspan=3)


def click(event):
    cap = cv2.VideoCapture(0)
    framewidth = 640
    frameheight = 480
    capbrightness = 130
    cap.set(3,framewidth)
    cap.set(4,frameheight)
    cap.set(10,capbrightness)

#object location detect krva mate
    def getContours(img):
        contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        x,y,w,h = 0,0,0,0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area>500:
                cv2.drawContours(img, cnt, -1, (255,0,0), 3)
                peri = cv2.arcLength(cnt, True)
                
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                x,y,w,h = cv2.boundingRect(approx)
                
        return x+w//2,y
        
    #creating list of points to draw 
    myPoints = []
   
    
                
    #creating function to draw
    def draw(myPoints):
        for points in myPoints:
            cv2.circle(img,(points[0],points[1]),3,(blue,green,red),cv2.FILLED)
     
    #detecting color
    
    min_HSV = np.array([70, 108, 187], dtype = "uint8")
    max_HSV = np.array([172, 255, 255], dtype = "uint8")
    
    
    #streaming video capture:
        
    if (cap.isOpened()== False):
        print("can't open stream")
    
    
    while (cap.isOpened()):
    
        ret, img = cap.read()
        newPoints=[]
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        skinRegionHSV = cv2.inRange(imgHSV, min_HSV, max_HSV)
        a,b=getContours(skinRegionHSV)
        cv2.circle(img,(a,b),2,(255,0,0),cv2.FILLED)
        if a!=0 and b!=0:
            newPoints.append([a,b])
        if len(newPoints)!=0:
            for newp in newPoints:
                myPoints.append(newp)
                
        blue = cv2.getTrackbarPos('Blue','color')
        green = cv2.getTrackbarPos('Green','color')
        red = cv2.getTrackbarPos('Red','color')
        
        print(blue,green,red)
        if len(myPoints)!=0:
            draw(myPoints)
        skinHSV = cv2.bitwise_and(img, img, mask = skinRegionHSV)
        if ret == True:
             #cv2.imshow('webCam',skinHSV)
             cv2.imshow('result',img)
             
             if cv2.waitKey(1) & 0xFF == ord('q'):
                 break
        else:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    


      
btn_open_webcam = tk.Button(r,text='WebCam')
btn_open_webcam.bind('<Button-1>',click)
btn_open_webcam.grid(row=2,columnspan=3)


label_color = tk.Label(r,text='choose color to draw on air :')
label_color.grid(row=3,columnspan=3)



r.mainloop()
