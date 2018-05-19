FROM jjanzic/docker-python3-opencv:contrib-opencv-3.4.1
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install numpy

#copy project directory
COPY ./ /usr/src/app
WORKDIR /usr/src/app

CMD ["python", "./app.py"]