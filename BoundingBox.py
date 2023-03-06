## [trackbar]
from __future__ import print_function
import cv2 
import numpy as np
import argparse
import random as rng

# Load source image
parser = argparse.ArgumentParser(description='Code for Creating Bounding boxes and circles for contours tutorial.')
parser.add_argument('--input', help='Path to input image.', default='3.jpg')
args = parser.parse_args()

img = cv2.imread(cv2.samples.findFile(args.input))

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply thresholding on the gray image to create a binary image
ret,thresh = cv2.threshold(gray,127,255,0)
thresh=255-thresh
# find the contours
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
s_cont=sorted(contours,key=cv2.contourArea,reverse=True)

# take the first contour
cnt = contours[0]

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)

# compute the bounding rectangle of the contour


# draw contour
#img = cv2.drawContours(img,[cnt],0,(0,255,255),2)
print(box)
# draw the bounding rectangle
#img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


# display the image with bounding rectangle drawn on it
cv2.imshow("Bounding Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()