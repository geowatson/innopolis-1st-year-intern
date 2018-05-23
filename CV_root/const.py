import cv2

subjects = ["", 'Pavlo', 'Joj0']
face_lbp_casc_path = 'opencv-files/lbpcascade_frontalface.xml'
face_haar_casc_path = 'opencv-files/haarcascade_frontalface_default.xml'
eye_haar_casc_path = 'opencv-files/haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_haar_casc_path)
eye_cascade = cv2.CascadeClassifier(eye_haar_casc_path)