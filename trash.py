import cv2 as cv 
import numpy as np 

img = cv.imread('images/bookpage.jpg')

#applying threshold
retval, threshold = cv.threshold(img, 12, 255, cv.THRESH_BINARY)
cv.imshow('thresh', threshold)
cv.waitKey(0)
cv.destroyAllWindows()
