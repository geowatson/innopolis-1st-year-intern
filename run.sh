#comand to build image (name:cv_root) of application in CV_root
docker build ./CV_root/ -t cv_root
docker run -d cv_root 10.91.42.90:8080 10.91.34.72:8080 30

#docker-compose up


