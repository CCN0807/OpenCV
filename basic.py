import cv2 as cv

img = cv.imread('Sources/tkt.jpg')
cv.imshow('TKt', img)

#Converting img to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Blur an img
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
cany = cv.Canny(blur, 125, 125,)
cv.imshow('Canny edge', cany)

#Dilating the image
dilated = cv.dilate(cany, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#Erolling
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eeolled', eroded)

#Resize
resized = cv.resize(img, (500,500))
cv.imshow('resize', resized)

#croop
croop = img[50:200, 100:300]
cv.imshow('Croop', croop)

cv.waitKey(0)