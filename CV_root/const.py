import cv2

subjects = ["", "Shahrukh Khan", "Elvis", "Tom Cruise", "Dicaprio", 'Pavlo']
lbp_casc_path = 'opencv-files/lbpcascade_frontalface.xml'
haar_casc_path = 'opencv-files/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_casc_path)