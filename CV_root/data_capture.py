import os
import cv2
import time
import math
from normalizator import normalize
from face_trace import detect_faces

def get_path(shape):
    path = []
    center = (int(shape[1] / 2), int(shape[0] / 2))
    r1 = max(shape) / 32
    r2 = max(shape) / 16
    path.append(center)
    for t in range(8):
        x = int(center[0] + r1 * math.cos(math.pi * t / 4))
        y = int(center[1] + r1 * math.sin(math.pi * t / 4))
        path.append((x, y))
    for t in range(8):
        x = int(center[0] + r2 * math.cos(math.pi * t / 4))
        y = int(center[1] + r2 * math.sin(math.pi * t / 4))
        path.append((x, y))
    return path, center


def data_capture1(n, data_folder_path='training-data'):
    """
    in progress
    :param n:
    :param data_folder_path:
    :return:
    """
    dirs = os.listdir(data_folder_path)

    if 's' + n not in dirs:
        os.mkdir(data_folder_path + '/s' + n)

    dir_name = data_folder_path + '/s' + n

    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    path, center = get_path(frame.shape)

    t = divmod(int(time.time() / 4), 10)[1]
    t2 = divmod(int(time.time() / 2), 10)[1]
    counter = 0
    colore = (255, 255, 0)
    dele = int(time.time()) + 8
    penalty = False

    while True:
        try:
            ret, frame = video_capture.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            pic = frame.copy()

            point = path[counter]
            cv2.rectangle(frame, point, point, colore, 8)
            cv2.rectangle(frame, center, center, colore, 8)

            cv2.imshow('Video', cv2.flip(frame, 1))
            if dele < int(time.time()):

                if int(time.time()) - t2 > 2:
                    colore = (0, 0, 255)
                    flag, pic = normalize(pic)
                    faces = detect_faces(pic)

                    if len(faces) == 0 or not flag:
                        penalty = True
                        continue

                    (x, y, w, h) = faces[0]

                    pic = pic[y:y + w, x:x + h]
                    cv2.imwrite(dir_name + '/' + str(counter) + '_'+str(point)+'.jpg', pic)

                if t != divmod(int(time.time() / 4), 10)[1]:
                    t = divmod(int(time.time() / 4), 10)[1]
                    t2 = int(time.time())
                    if not penalty:
                        counter += 1
                    else:
                        penalty = False
                    if counter >= len(path):
                        exit()
                    point = path[counter]
                    colore = (255, 255, 0)
                    flag = True

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except KeyError:
            continue

    video_capture.release()
    cv2.destroyAllWindows()


def data_capture2(n, data_folder_path='training-data'):
    """

    :param n:
    :param data_folder_path:
    :return:
    """
    count = 100
    dirs = os.listdir(data_folder_path)

    if 's' + n not in dirs:
        os.mkdir(data_folder_path + '/s' + n)

    dir_name = data_folder_path + '/s' + n

    video_capture = cv2.VideoCapture(0)

    while count:
        ret, frame = video_capture.read()
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        flag, gray_img = normalize(gray_img)

        faces = detect_faces(gray_img)

        if len(faces) == 0 or not flag:
            continue

        (x, y, w, h) = faces[0]

        save = gray_img[y:y + w, x:x + h]
        cv2.imwrite(dir_name + '/' + str(count) + '.jpg', save)
        count -= 1


n = input()
data_capture2(n)
