import cv2
import socket
import time
from const import subjects, face_cascade, eye_cascade, smile_cascade


def detect_faces(gray_img):
    """
    Method uses face_cascade to capture face on image
    :param img: image with faces
    :return: list of coordinates of captured faces
    """
    faces = face_cascade.detectMultiScale(
        gray_img,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(300, 300),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return faces


def detect_eyes(gray_img):
    """
    Method uses face_cascade to capture face on image
    :param img: image with faces
    :return: list of coordinates of captured faces
    """
    faces = eye_cascade.detectMultiScale(
        gray_img,
        scaleFactor=1.3,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return faces


def video_stream():
    """
    Method to start wide stream with face stream
    :return: None
    """
    video_capture = cv2.VideoCapture(0)

    # watch ip camera stream
    while True:
        try:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # looking for faces in frame
            eyes = detect_eyes(frame)
            faces = detect_faces(frame)

            # Draw a rectangle around the faces
            if len(eyes) == 2:
                for (x, y, w, h) in eyes:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except KeyError:
            continue

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()