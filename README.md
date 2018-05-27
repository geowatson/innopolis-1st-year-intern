# innopolis-1st-year-intern
dev
v1.2

## Usage:
Put local `host ip` in `door_example/app.py` and run it to launch server.

Put parameters (`door_ip`, `cam_ip`, `accuracy`) in run.sh and launch it (Docker install require).

Done. You will see massages in `door_example/app.py` console

## CV_root
### Usage:
command `python app.py` will launch face recognition based on faces in `training-data` folder,
command `python capture.py` will launch face writing in `training-data` folder

#### Files:
`api_pattern` : class Door to send massages on server

`app.py` : core file, which launch all program.

`const.py` : file store labels and paths to templates.

`data_capture.py` : file store script of automate face capturing for `training-data`.

`face_trace.py` : file contains methods to recognize parts of face.

`normalizator.py` : file contains method to normalize face by eyes line.

`recognizer.py` : file contains main engine of face recognition.