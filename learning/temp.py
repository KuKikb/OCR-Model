from turtle import clear
import numpy as np
import cv2
from PIL import Image
import os
import imutils
import matplotlib.pyplot as plt

#create a copy for manipulation
# copy = Image.open('text_image.png')
# copy.save('copy.png')

copy = cv2.imread(r'D:\snippy\learning\text_image.png')
cv2.imwrite('copy.png', copy)

#convert black charachters to red
img = Image.open('copy.png').convert('RGB')
data = np.array(img)
data[(data == (0,0,0)).all(axis = -1)] = (255,0,0)
img = Image.fromarray(data, mode='RGB')
img.save('copy.png')

# Read input image
img = cv2.imread('copy.png')

# Convert from BGR to HSV color space
hsv2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

thresh2 = cv2.bitwise_not(hsv2)

# Get the saturation plane - all black/white/gray pixels are zero, and colored pixels are above zero.
hsv = hsv[:,:,1]
# Apply threshold on s - use automatic threshold algorithm (use THRESH_OTSU).
ret, thresh = cv2.threshold(hsv, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

thresh += thresh2

cv2.imshow("",thresh)
# Find contours in thresh (find only the outer contour - only the rectangle).
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # [-2] indexing takes return value before last (due to OpenCV compatibility issues).

# Find contours in thresh (find the triangles).f
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # [-2] indexing takes return value before last (due to OpenCV compatibility issues).

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 3))
dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)
cv2.imshow('dilation', dilation)

contours_line = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]

print(len(contours_line))
im2 = img.copy()

line = []
 
for cnt in contours_line:
        x, y, w, h = cv2.boundingRect(np.asarray(cnt))
        line.append(y+h)
        print(x,y,w,h)
        cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

no_of_lines = len(line)
print(no_of_lines)
print(len(contours))

left = []
right = []
top = []
bottom = []


for c in contours:
        
        left.append(tuple(c[c[:, :, 0].argmin()][0])[0] - 2) #takin additional 2 pixel area for better
        right.append(tuple(c[c[:, :, 0].argmax()][0])[0] + 2)
        top.append(tuple(c[c[:, :, 1].argmin()][0])[1] - 2)
        bottom.append(tuple(c[c[:, :, 1].argmax()][0])[1] + 2)


left.sort()
right.sort()
top.sort()
bottom.sort()

print(top,type(top[0]),len(top))
print(bottom, len(bottom))
print(left, len(left))
print(right, len(right))

i = 0
while(i <= len(left)-2):
        if(len(left) >= 2):
                
                if(left[i+1] <= left[i]+5 or right[i+1] <= right[i]+5):
                        print(left[i], left[i+1])
                        print(right[i], right[i+1])
                        print(left.remove(left[i]),"\t",i)
                        print(right.remove(right[i]),"\t",i)      
        i += 1


print(left, len(left))
print(right, len(right))

length = bottom[-1] - top[0] # randomly picked a character to get a height estimate
print(length)


plt.imshow(im2, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.imshow(thresh, cmap = 'gray')


# plt.imshow(thresh)
cv2.waitKey(0)
plt.show()