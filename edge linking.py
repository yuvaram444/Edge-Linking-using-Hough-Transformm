# In[ ]:## Read image and convert it to grayscale image
## Developed by : 
## Reg no : 
import cv2
import numpy as np
import matplotlib.pyplot as plt
image1=cv2.imread('.jpg',0)
img= cv2.GaussianBlur()
plt.imshow(img)

## Find the edges in the image using canny detector and display
## Developed by :
## Reg no : 
edges1 = cv2.Canny(img,)
plt.imshow(edges1,cmap = 'gray')
plt.title('Edge Image'), plt.xticks()
plt.show()

## Detect points that form a line using HoughLinesP
## Developed by : 
## Reg no :
lines=cv2.HoughLinesP(edges1,1,np.pi/180, threshold=80, minLineLength=50,maxLineGap=250)

## Draw lines on the image
## Developed by : 
## Reg no : 
for line in lines:
    x1, y1, x2, y2 = line [0] 
    cv2.line(edges1,(x1, y1),,3)



## Display the result
## Developed by :
## Reg no : 
plt.imshow(edges1)

