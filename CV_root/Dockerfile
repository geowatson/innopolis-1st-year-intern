FROM jjanzic/docker-python3-opencv
RUN pip install --upgrade pip
RUN pip install requests

#copy project directory
COPY ./ /usr/src/app
WORKDIR /usr/src/app

CMD ["python", "./app.py"]