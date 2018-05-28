import cv2
import numpy as np
from face_trace import detect_faces, detect_eyes


# TODO nose tracking
def normalize(gray_img):
    """
    Method normalize gray_img by line of eyes
    :param gray_img:
    :return: Flag - Are there eyes or not, normalize picture
    """
    eyes = detect_eyes(gray_img)

    if len(eyes) == 2:
        x_s = []
        y_s = []
        for (x, y, w, h) in eyes:
            x_s.append(x + int(w / 2))
            y_s.append(y + int(h / 2))

        face_center = (np.mean(x_s, dtype='int'), np.mean(y_s, dtype='int'))

        if face_center[0] > x_s[0]:
            left_eye = (x_s[0], y_s[0])
            right_eye = (x_s[1], y_s[1])
        else:
            left_eye = (x_s[1], y_s[1])
            right_eye = (x_s[0], y_s[0])

        # compute the angle between the eye centroids
        dX = left_eye[0] - right_eye[0]
        dY = left_eye[1] - right_eye[1]
        angle = np.degrees(np.arctan2(dY, dX)) - 180

        # to avoid miss prediction
        if angle >= -50 or angle <= -310:
            M = cv2.getRotationMatrix2D(face_center, angle, 1)

            # rotate matrix
            return True, cv2.warpAffine(gray_img, M, dsize=(gray_img.shape[1], gray_img.shape[0]), flags=cv2.INTER_CUBIC)

    return False, gray_img


def normalize_video_stream():
    video_capture = cv2.VideoCapture(0)

    # watch ip camera stream
    while True:
        try:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # normalization
            flag, frame = normalize(frame)

            faces = detect_faces(frame)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except KeyError:
            continue

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

