import cv2 as cv
import numpy as np

img = cv.imread('Sources/tkt.jpg')

#Translation
def Translation(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimenstion = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimenstion)

# -x --> left
# x --> right
# -y --> up
# y --> down

translation = Translation(img, -10, -10)
cv.imshow('translation', translation)

# Rotation
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimenstions = (width, height)
    return cv.warpAffine(img, rotMat, dimenstions)

rotated = rotate(img, 10)
cv.imshow('rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flip
# 0 = Horizontally
# 1 = Vertically
# -1 = Vertically and Horizontally
flip = cv.flip(img, -1)
cv.imshow('flip', flip)

#Crooping
cropped = img[10:30, 30:40]
cv.imshow('crop', cropped)

cv.waitKey(0)