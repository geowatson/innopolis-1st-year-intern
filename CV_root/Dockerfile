#FROM jjanzic/docker-python3-opencv:contrib-opencv-3.4.1
FROM python:3
RUN pip install --upgrade pip
RUN pip install opencv-contrib-python
RUN pip install requests
RUN pip install numpy

#copy project directory
COPY ./ /usr/src/app
WORKDIR /usr/src/app

ENTRYPOINT ["python", "./app.py"]

# 10.91.42.90:8080 10.91.34.72:8080 30