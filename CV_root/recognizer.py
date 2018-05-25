import cv2
import os
import numpy as np
from const import subjects, face_cascade
from face_trace import detect_faces
from api_pattern import Camera


class Recognizer:
    """
    Class responsible for detecting and reporting of person
    """
    def __init__(self, cam_ip):
        ##### STEP 1 ##### - Prepare image data set
        faces, labels = self.prepare_training_data()
        ##### STEP 2 ##### - Create new instance of recognizer
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        ##### STEP 3 ##### - Train recognizer on data set
        recognizer.train(faces, np.array(labels))
        ##### STEP 4 ##### - Recognizer ready to recognize
        self.recognizer = recognizer
        self.camera = Camera(ip=cam_ip, door_id=1)

    def detect_face(self, img):
        """
        Method uses face_cascade to capture face on image
        :param img: image with face
        :return: face image and its coordinates if found None otherwise
        """
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray_img,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if (len(faces) == 0):
            return None, None

        (x, y, w, h) = faces[0]

        return gray_img[y:y + w, x:x + h], faces[0]

    def prepare_training_data(self, data_folder_path="training-data"):
        """
        Method goes through all images in data_folder_path and detect faces on them
        :param data_folder_path: path to folder with objects images
        :return: faces vector and label vector
        """

        faces = []
        labels = []

        # goes through main folder
        for folder in os.listdir(data_folder_path):

            if not folder.startswith("s"):
                continue;

            subject_label = int(folder.replace("s", ""))

            subject_dir_path = data_folder_path + "/" + folder

            # goes through sub folder of object
            for image_name in os.listdir(subject_dir_path):

                if image_name.startswith("."):
                    continue;

                image_path = subject_dir_path + "/" + image_name
                image = cv2.imread(image_path)

                face, rect = self.detect_face(image)

                if face is not None:
                    faces.append(face)
                    labels.append(subject_label)

        return faces, labels

    def predict_obj(self, base_img):
        """
        Method detect face on the base_img and put it into recognizer
        if person in database, send request to the client door
        :param base_img: image to recognize
        :return: base_img with label if recognized
        """

        grey_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2GRAY)
        # looking for faces in frame
        faces = detect_faces(grey_img)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            # predict person
            label = self.recognizer.predict(grey_img[y:y + w, x:x + h])

            # print face prediction
            if label[1] < 30.0:
                label_text = subjects[label[0]]
                # confirmation of the person
                # camera.success(name=label_text)

                # For test streaming
                cv2.putText(base_img, label_text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 1.7, (0, 0, 255), 2);
                cv2.rectangle(base_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
