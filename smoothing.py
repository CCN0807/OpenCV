import cv2 as cv
import numpy as np

img = cv.imread('Sources/tkt.jpg')
cv.imshow('tkt', img)

#Averageing
Average = cv.blur(img, (3,3))
cv.imshow('Average blur', Average)

#Gaussian blur
Gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', Gaussian)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#Natural blur/ bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 250)
cv.imshow('Bilateral', bilateral)

if 0xFF == ord('d'):
    cv.destroyAllWindows()

cv.waitKey(0)