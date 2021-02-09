import cv2 as cv
import numpy as np

#width, height and number of color channel e.g.(0,0,255) -->3
blank = np.zeros((500,500, 3), dtype='uint8')


#1. Paint the img in certain colour
blank[200:300, 300:400] = 0,255,255


# 2. Draw a rectangle
cv.rectangle(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,0,255), thickness=-1)


# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,0,0), thickness=-1)


#4. Draw a line
cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)

# 5. Write text
cv.putText(blank, 'Hello', (225,255), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0), thickness = 2)
cv.imshow('text', blank)

img = cv.imread('Sources/tkt.jpg')
cv.imshow('TKT', img)

cv.waitKey(0)