import cv2
import os
import numpy as np
import socket
import time

subjects = ["", "Shahrukh Khan", "Elvis", "Tom Cruise", "Pavlo"]
casc_path = 'opencv-files/lbpcascade_frontalface.xml'
face_cascade = cv2.CascadeClassifier(casc_path)

print('start')

def detect_face(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5);

    if (len(faces) == 0):
        return None, None

    (x, y, w, h) = faces[0]

    return cv2.resize(gray_img[y:y + w, x:x + h], (600, 500)), faces[0]


def prepare_training_data(data_folder_path="training-data"):
    dirs = os.listdir(data_folder_path)

    faces = []
    labels = []

    for dir_name in dirs:

        if not dir_name.startswith("s"):
            continue;

        label = int(dir_name.replace("s", ""))

        subject_dir_path = data_folder_path + "/" + dir_name

        subject_images_names = os.listdir(subject_dir_path)

        for image_name in subject_images_names:

            if image_name.startswith("."):
                continue;

            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)

            face, rect = detect_face(image)

            if face is not None:
                faces.append(face)
                labels.append(label)

    return faces, labels


faces, labels = prepare_training_data()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))
video_capture = None

print('Training done')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("", 5000))
server_socket.listen(5)


# wait for ip camera url
while True:
    try:
        client_socket, address = server_socket.accept()
        print("Conencted to - ", address, "\n")
        cam_url = client_socket.recv(1024).decode("utf-8")
        print(cam_url)
        video_capture = cv2.VideoCapture(cam_url)
        break

    except socket.timeout:
        continue
    #except Exception:
        #server_socket.close()

# watch ip camera stream
while True:
    try:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if not frame:
            pass

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # looking for faces in frame
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:

            label = face_recognizer.predict(gray[y:y + w, x:x + h])
            if label[1] > 30.0:
                continue
            print(subjects[label[0]])
            print(label[1])
            time.sleep(4)

            #label_text = subjects[label[0]]
            #cv2.putText(frame, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        #frame = cv2.resize(frame, (600, 500))
        #cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except KeyError: #cv2.error:
        continue
    except ValueError:
        print(video_capture.isOpened())
        time.sleep(4)
        continue

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()