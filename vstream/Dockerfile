FROM jjanzic/docker-python3-opencv
RUN pip install --upgrade pip

# copy project directory
COPY ./ /usr/src/app
WORKDIR /usr/src/app

RUN apt-get install -y streamer fswebcam
# RUN xhost +
# RUN streamer -f jpeg -c /dev/video0 -o ./img.jpg
# RUN streamer -o foobar.jpeg
# RUN mknod /dev/video0 c 81 0
# RUN lsmod|grep uvcvideo
# RUN fswebcam -r 640x480 --no-banner image3.jpg
CMD ["python", "./s.py"]
