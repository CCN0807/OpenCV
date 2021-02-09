import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Sources/tkt.jpg')
cv.imshow('tkt', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

#GrayScale histogram
""""
gray_hist = cv.calchist([gray], [0], mask, [256], [0, 500])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
"""
# Color histogram

plt.figure()
plt.title('Colour` histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ['b', 'g', 'r']
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 500])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


if 0xFF == ord('d'):
    cv.destroyAllWindows()

cv.waitKey(0)