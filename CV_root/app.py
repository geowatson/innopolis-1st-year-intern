import cv2
from recognizer import get_recognizer
from const import subjects, face_cascade
from face_trace import detect_faces
from normalizator import normalize


def predict_obj(img):
    # looking for faces in frame
    faces = detect_faces(frame)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        # predict person
        label = face_recognizer.predict(img[y:y + w, x:x + h])

        # print face prediction
        if label[1] < 25.0:
            label_text = subjects[label[0]]
            cv2.putText(img, label_text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


face_recognizer = get_recognizer()

video_capture = cv2.VideoCapture(0)

# watch ip camera stream
while True:
    try:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        predict_obj(frame)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except KeyError:
        continue

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()