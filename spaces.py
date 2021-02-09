import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('Sources/tkt.jpg')
cv.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

# BGR to Gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*B
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()
if 0xFF == ord('d'):
    cv.destroyAllWindows()
cv.waitKey(0)