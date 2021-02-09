import cv2 as cv

img = cv.imread('Sources/tkt.jpg')

cv.imshow('LOve ice-cream', img)

capture = cv.VideoCapture('Sources/video_2.4e_01.mpg')

"""""
while True:
    isTure, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
"""""
cv.waitKey(0)
