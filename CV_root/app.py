import cv2
import sys
from recognizer import Recognizer


door_ip = '10.91.36.52:8080'


face_recognizer = Recognizer(door_ip)

video_capture = cv2.VideoCapture(0)

# watch ip camera stream
while True:
    try:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # predict person on the frame
        face_recognizer.predict_obj(frame)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except KeyError:
        continue

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()