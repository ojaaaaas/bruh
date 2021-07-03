import cv2 as cv 
import numpy as np 

img1 = cv.imread('images/3D-Matplotlib.png')
img2 = cv.imread('images/mainsvmimage.png')

# add = img1 + img2 
# add = cv.add(img1,img2)
weighted = cv.addWeighted(img1, 1, img2, 0, 0)



cv.imshow('weighted', weighted)
cv.waitKey(0)
cv.destroyAllWindows()