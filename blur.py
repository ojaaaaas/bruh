import cv2 as cv 
import numpy as np

#capturing video from webcam
cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #hsv values - hue saturation value
    lower_blue = np.array([100,100,0])
    upper_blue = np.array([180,255,255])

    mask = cv.inRange(hsv, lower_blue, upper_blue)
    res = cv.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv.filter2D(res, -1, kernel)
    #gaussian blur
    blur = cv.GaussianBlur(res, (15,15), 0)
    #median blur
    median = cv.medianBlur(res, 15)





    cv.imshow('frame', frame)
    # cv.imshow('mask', mask)
    cv.imshow('res', res)
    #smoothening
    # cv.imshow('smooth',smoothed)
    #gblur
    # cv.imshow('blur',blur)
    #mblur
    cv.imshow('median', median)
    

    if cv.waitKey(1) & 0xFF==ord('q'):
        break
    

cv.destroyAllWindows()
cap.release()
