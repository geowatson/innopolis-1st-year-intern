FROM jjanzic/docker-python3-opencv
RUN pip install --upgrade pip
RUN pip install requests

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["python", "./app.py"]