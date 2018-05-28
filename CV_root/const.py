import cv2

subjects = ["", 'Pavel [Developer]', 'Georg [Developer]', "Julia", 'Andry']
face_lbp_casc_path = 'opencv-files/lbpcascade_frontalface.xml'
face_haar_casc_path = 'opencv-files/haarcascade_frontalface_default.xml'
eye_haar_casc_path = 'opencv-files/haarcascade_eye.xml'
eye_tree_haar_casc_path = 'opencv-files/haarcascade_eye_tree_eyeglasses.xml'
smile_haar_casc_path = 'opencv-files/haarcascade_smile.xml'
face_cascade = cv2.CascadeClassifier(face_haar_casc_path)
eye_cascade = cv2.CascadeClassifier(eye_tree_haar_casc_path)
smile_cascade = cv2.CascadeClassifier(smile_haar_casc_path)