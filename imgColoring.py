import cv2

img = cv2.imread('cat.jpg')
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurimg = cv2.GaussianBlur(img,(7,7),0)
edge = cv2.Canny(img,100,100)

cv2.imshow('normal',img)
cv2.imshow('gray',grayimg)
cv2.imshow('blur',blurimg)
cv2.imshow('edge',edge)

cv2.waitKey(5000)
cv2.destroyAllWindows()
   
    

