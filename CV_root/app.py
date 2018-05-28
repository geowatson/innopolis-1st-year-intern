from recognizer import Recognizer
import sys
import cv2


# parameters for connection (door_ip, cam_ip, accuracy)
try:
    door_ip = sys.argv[1]
    cam_ip = sys.argv[2]
    accuracy = float(sys.argv[3])
except IndexError:
    print("some of parameters wasn't detected (door_ip, cam_ip, accuracy)")
    print(len(sys.argv))
    exit(1)


face_recognizer = Recognizer(door_ip, accuracy)

video_capture = cv2.VideoCapture('http://'+cam_ip)

# watch ip camera stream
while True:
    try:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # predict person on the frame
        face_recognizer.predict_obj(frame)

        # Display the resulting frame (optional)
        # cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except KeyError:
        continue

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()