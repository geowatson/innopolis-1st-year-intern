import cv2
import os
import numpy as np
from const import subjects, face_cascade


def get_recognizer():
    ##### STEP 1 ##### - Prepare image data set
    faces, labels = prepare_training_data()
    ##### STEP 2 ##### - Create new instance of recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    ##### STEP 3 ##### - Train recognizer on data set
    recognizer.train(faces, np.array(labels))
    ##### STEP 4 ##### - Recognizer ready to recognize
    return recognizer


def detect_face(img):
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


def prepare_training_data(data_folder_path="training-data"):
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

            face, rect = detect_face(image)

            if face is not None:
                faces.append(face)
                labels.append(subject_label)

    return faces, labels
