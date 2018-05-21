import os
import cv2
import time

data_folder_path = 'training-data'

dirs = os.listdir(data_folder_path)

n = input()

if 's'+n not in dirs:
    os.mkdir(data_folder_path+'/s'+n)

dir_name = data_folder_path+'/s'+n

video_capture = cv2.VideoCapture(0)

for i in range(50):
    ret, frame = video_capture.read()
    cv2.imwrite(dir_name+'/'+str(i)+'.jpg', frame)
    time.sleep(0.5)


