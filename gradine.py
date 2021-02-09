import cv2 as cv 
import numpy as np

img = cv.imread('Sources/tkt.jpg')
cv.imshow('tkt', img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('gray', gray)

#Loplocation
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap', lap)

#Sabel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('Combine', combine_sobel)

cv.waitKey(0)