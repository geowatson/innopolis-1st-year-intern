import cv2
from recognizer import get_recognizer
from const import subjects, face_cascade
from face_trace import detect_faces
from api_pattern import Camera


def predict_obj(base_img):
    """
    Method detect face on the base_img and put it into face_recognizer
    :param base_img: image to recognize
    :return: base_img with label if recognized
    """

    grey = cv2.cvtColor(base_img, cv2.COLOR_BGR2GRAY)
    # looking for faces in frame
    faces = detect_faces(grey)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        # predict person
        label = face_recognizer.predict(grey[y:y + w, x:x + h])

        # print face prediction
        if label[1] < 30.0:
            label_text = subjects[label[0]]
            #camera.success(name=label_text)
            cv2.putText(base_img, label_text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 1.7, (0, 0, 255), 2);
            cv2.rectangle(base_img, (x, y), (x + w, y + h), (0, 255, 0), 2)


face_recognizer = get_recognizer()
cam = 'http://192.168.0.37:8080'
video_capture = cv2.VideoCapture(0)

#camera = Camera(ip='169.254.213.201:8080', door_id=1)

# watch ip camera stream
while True:
    try:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

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