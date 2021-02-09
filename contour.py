import numpy as np
import cv2 as cv

img = cv.imread('Sources/tkt.jpg')
cv.imshow('TKT', img)

blank = np.zeros(img.shape, dtype= 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

Blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(Blur, 125, 175)
cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (255,255,255), 1)
cv.imshow('Contour draw', blank)


if 0xFF==ord('d'):
    cv.destroyAllWindows()
cv.waitKey(0)