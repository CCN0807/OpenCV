import cv2 as cv

img = cv.imread('Sources/tkt.jpg')
cv.imshow('tkt', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding
treshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

#Inverted
treshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Iverted Threshold', thresh_inv)

#Adoptive Thresholding
adaptive = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive', adaptive)

cv.waitKey(0)
