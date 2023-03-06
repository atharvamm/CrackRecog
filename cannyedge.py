import cv2
import numpy as np
path=str(input('input path to image: \n'))
img = cv2.imread(path)
cv2.imshow('Original', img)
cv2.waitKey(0)
#Function to convert image from black background to white background
def invert(imagem):
    imagem = (255-imagem)
    return imagem
#Converting image to gray before applying sobel filter
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Applying Gaussian Blur before Canny Filter
img_blur = cv2.GaussianBlur(img_gray, (3,3),cv2.BORDER_DEFAULT)

def sobelinx(img):
    gy = np.array([[-1.,-2.,-1.],[0.,0.,0.],[1.,2.,1.]])
    gx = gy.T
    dst = cv2.filter2D(img, -1, gx)
    return dst
def sobeliny(img):
    gy = np.array([[-1.,-2.,-1.],[0.,0.,0.],[1.,2.,1.]])
    gx = gy.T
    dst = cv2.filter2D(img, -1, gy)
    return dst

sobely1=sobeliny(img_gray)
sobelx1=sobelinx(img_gray)
abs_grad_x = cv2.convertScaleAbs(sobelx1)
abs_grad_y = cv2.convertScaleAbs(sobely1)  
#Combining Sobel X and Sobel Y
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
grad=invert(grad)
cv2.imshow('Sobel self X', sobelx1)
cv2.waitKey(0)
cv2.imshow('Sobel self Y', sobely1)
cv2.waitKey(0)
cv2.imshow('Combined Sobel function', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()
path2=path.replace(".png","-sobel.png")
cv2.imwrite(path2,grad)
cv2.namedWindow('CannyEdgeDetector')
# define a null callback function for Trackbar
def null(x):
     pass
cv2.createTrackbar("LowerThreshold", "CannyEdgeDetector", 0, 255, null)
cv2.createTrackbar("UpperThreshold", "CannyEdgeDetector", 0, 255, null)
cv2.createTrackbar("ApertureSize", "CannyEdgeDetector", 3, 7, null)
while True:
    
     # read the Trackbar positions
     l = cv2.getTrackbarPos('LowerThreshold','CannyEdgeDetector')
     u = cv2.getTrackbarPos('UpperThreshold','CannyEdgeDetector')
     a = cv2.getTrackbarPos('ApertureSize','CannyEdgeDetector')
     edges = cv2.Canny(image=img_blur, threshold1=l, threshold2=u,apertureSize=a)
     edges=invert(edges)
     # display trackbars and image
     cv2.imshow('CannyEdgeDetector', edges)
     if cv2.waitKey(1) & 0xFF==ord('q'):
         break


path1=path.replace(".png","-canny.png")
cv2.imwrite(path1,edges)
cv2.destroyAllWindows() 

