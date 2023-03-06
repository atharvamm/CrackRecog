# importing necessary libraries
import numpy as np
from skimage.color import rgb2gray
from skimage.io import imread
from skimage import feature, img_as_bool
from skimage.morphology import binary_dilation, binary_erosion
import matplotlib.pyplot as plt
import cv2

def disp_img(img,win_name= "Name"):
    cv2.imshow(win_name,img)
    cv2.waitKey(0)

def make_image_collage(img_list):
    try:
        if len(img_list)%2 == 0:
            pass
        else:
            img_list.append(img_list[0].copy())
        
        row1 = np.hstack(img_list[0:len(img_list)//2])
        row2 = np.hstack(img_list[len(img_list)//2:])

        final_image = np.vstack([row1,row2])
        disp_img(final_image)

    except ValueError:
        print("The shape of your images dont match.")
        for i in img_list:
            print(i.shape)

def preprocess(url):
    img = imread(url)
    # img = rgb2gray(img)
    img = cv2.medianBlur(img,5)
    img_edge = binary_erosion(binary_dilation(feature.canny(img, sigma =.1)))
    return img, img_edge

def edge_prob(window, cut_off):
    pixels  = np.array(window.ravel())
    if ((np.count_nonzero(pixels)/len(pixels))>cut_off):
        return 1
    else:
        return 0
    
def sliding_mat(img,window_x=10,window_y=10, cut_off=0.1):
    
    arr_x = np.arange(0,img.shape[0],window_x)
    arr_y = np.arange(0,img.shape[1],window_y)

    A = np.zeros((len(arr_x),len(arr_y)))

    for i,x in enumerate(arr_x):
        for j,y in enumerate(arr_y):
            window = img[x:x+window_x,y:y+window_y]
            A[i,j] = edge_prob(window, cut_off=cut_off)
    
    return A, arr_x, arr_y

def plot_all(img,canny_edge,A):
    fig = plt.figure(figsize = (9,4))
    ax1 = fig.add_subplot(131)
    ax1.imshow(img, cmap="gray")
    ax1.set_title("Original")
    
    ax2 = fig.add_subplot(132)
    ax2.set_title("Canny Edge Detection")
    ax2.imshow(canny_edge, cmap="gray")
    
    ax3 = fig.add_subplot(133)
    ax3.set_title("Mask")
    ax3.imshow(A,cmap="gray")
    plt.tight_layout()
    plt.show()


url = "concrete_crack_images/cropped_00000019.png"
img1 = imread(url)

img1,c1 = preprocess(url)

make_image_collage([img1,c1])

A, arr_x, arr_y = sliding_mat(c1, window_x=10, window_y=10, cut_off=0.1)

print("Estimate of crack : {:.2f}%".format(np.sum(A)/A.size*100))
plot_all(img1,c1,A)
# make_image_collage([img1,c1,A])

print("Shape of image {}\nShape of : A {}".format(c1.shape,A.shape))
plt.hist(A.ravel())
plt.show()




