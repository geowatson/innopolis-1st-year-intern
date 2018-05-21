import cv2

subjects = ["", "Shahrukh Khan", "Elvis", "Tom Cruise", "Dicaprio", 'Pavlo']
casc_path = 'opencv-files/lbpcascade_frontalface.xml'
casc_path2 = 'opencv-files/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(casc_path2)