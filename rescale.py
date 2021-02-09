import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #Video and images
    width = int(frame.shape[1] * scale)
    # frame.shape[1] = orginal width
    height = int(frame.shape[0] * scale)
    # frame.shape[0] = orginal height

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #only for live video
    capture.set(3,width)
    capture.set(4,width)

#Video source
capture = cv.VideoCapture('Sources/video_2.4e_01.mpg')
#Photo sourcce
img = cv.imread('Sources/tkt.jpg')
cv.imshow("original", img)
resizeImg = rescaleFrame(img, 1.5)
cv.imshow('LOL ice-cream', resizeImg)

while True:
    isTure, frame = capture.read()
    cv.imshow('Video', frame)

    frame_resized = rescaleFrame(frame)
    cv.imshow('VideoResize', frame_resized)

    #frame_reRees = changeRes(1,2)
    #cv.imshow("Video_changeRes", frame_reRees)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)