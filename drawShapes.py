import cv2
import numpy as np

img = np.zeros((500,600,3),np.uint8)
img[:] = 125,85,170
cv2.line(img,(100,100),(300,400),(123,45,52),2)
cv2.rectangle(img,(100,100),(300,400),(200,150,144),5)
cv2.circle(img,(300,250),30,(200,150,144),4)
cv2.putText(img,"POQ",(330,270),cv2.FONT_HERSHEY_SIMPLEX,2,(200,150,144))
 
cv2.imshow('zeros',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()