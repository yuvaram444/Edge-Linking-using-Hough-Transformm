# Edge-Linking-using-Hough-Transformm
## Aim:
To write a Python program to detect the lines using Hough Transform.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:

Import all the necessary modules for the program.
### Step2:

Load a image using imread() from cv2 module.
### Step3:

Convert the image to grayscale.
### Step4:

Using Canny operator from cv2,detect the edges of the image.
### Step5:

Using the HoughLinesP(),detect line co-ordinates for every points in the images.Using For loop,draw the lines on the found co-ordinates.Display the image.
## Output

### Input image and grayscale image
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("C:/Users/admin/OneDrive/Pictures/Screenshots/dragon.jpg")  # Replace with your image path
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Input Image')
plt.axis('off')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
```
![image](https://github.com/user-attachments/assets/77315144-64ab-4b1a-876b-97f7cb735cbd)
![image](https://github.com/user-attachments/assets/025cb720-93c7-4d26-89b1-b4d8fff29164)


### Canny Edge detector output
```
edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)
# Display Canny Edge Detection Output   
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detector Output')
plt.axis('off')
plt.show()
```
![image](https://github.com/user-attachments/assets/f8cd5b93-bc36-456a-a884-3236f28deedb)


### Display the result of Hough transform
```
# Detect lines using the probabilistic Hough transform
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=50, maxLineGap=10)

# Draw the lines on the original image
output_image = image.copy()

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
# Display Hough Transform Result
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title('Hough Transform - Line Detection')
plt.axis('off')
plt.show()
```
![image](https://github.com/user-attachments/assets/bd9751bc-c1e9-4f49-82b9-345d8962ad10)


