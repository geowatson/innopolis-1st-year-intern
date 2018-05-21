import cv2
import socket
import time
from recognizer import get_recognizer
from const import subjects, face_cascade

def detect_faces(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray_img,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return faces


face_recognizer = get_recognizer()

video_capture = cv2.VideoCapture(0)

# watch ip camera stream
while True:
    try:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # looking for faces in frame
        faces = detect_faces(frame)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            # predict person
            label = face_recognizer.predict(cv2.cvtColor(frame[y:y + w, x:x + h], cv2.COLOR_BGR2GRAY))

            # print face prediction
            if label[1] < 25.0:
                label_text = subjects[label[0]]
                cv2.putText(frame, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except KeyError:
        continue

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()