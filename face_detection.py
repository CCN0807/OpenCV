import cv2 as cv

img = cv.imread('Sources/classmeeting.jpg')

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

haar_cascade = cv.CascadeClassifier('hear_face.xml')

try:
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    if len(face_rect) == 0:
        print('No face was found')
    else:
        print(f'Faces detected: {len(face_rect)}')

        for (x, y, w, h) in face_rect:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)

            cv.imshow('Detected faces', img)

except:
    print('Error')


cv.waitKey(0)