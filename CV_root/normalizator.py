import cv2
import socket
import time
from recognizer import get_recognizer
from const import subjects, face_cascade, eye_cascade
import numpy as np
import math

def detect_faces(img):
    """
    Method uses face_cascade to capture face on image
    :param img: image with faces
    :return: list of coordinates of captured faces
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray_img,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(300, 300),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return faces


def detect_eyes(img):
    """
    Method uses face_cascade to capture face on image
    :param img: image with faces
    :return: list of coordinates of captured faces
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = eye_cascade.detectMultiScale(
        gray_img,
        scaleFactor=1.3,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return faces

video_capture = cv2.VideoCapture(0)


# watch ip camera stream
while True:
    try:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # looking for faces in frame
        eyes = detect_eyes(frame)

        # Draw a rectangle around the faces
        if len(eyes) == 2:
            x_s = []
            y_s = []
            for (x, y, w, h) in eyes:
                x_s.append(x + int(w/2))
                y_s.append(y + int(h/2))

            face_center = (np.mean(x_s, dtype='int'), np.mean(y_s, dtype='int'))

            if face_center[0] > x_s[0]:
                left_eye = (x_s[0], y_s[0])
                right_eye = (x_s[1], y_s[1])
            else:
                left_eye = (x_s[1], y_s[1])
                right_eye = (x_s[0], y_s[0])

            # compute the angle between the eye centroids
            dX = left_eye[0] - right_eye[0]
            dY = left_eye[1] - right_eye[1]
            angle = np.degrees(np.arctan2(dY, dX)) - 180

            # to avoid miss prediction
            if angle >= -50 or angle <= -310:

                M = cv2.getRotationMatrix2D(face_center, angle, 1)

                # rotate matrix
                frame = cv2.warpAffine(frame, M, dsize=(frame.shape[1], frame.shape[0]), flags=cv2.INTER_CUBIC)

        faces = detect_faces(frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)


        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except KeyError:
        continue

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()