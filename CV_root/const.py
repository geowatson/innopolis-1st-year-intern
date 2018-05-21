import cv2

subjects = ["", "Shahrukh Khan", "Elvis", "Tom Cruise", "Dicaprio"]
casc_path = 'opencv-files/lbpcascade_frontalface.xml'
face_cascade = cv2.CascadeClassifier(casc_path)