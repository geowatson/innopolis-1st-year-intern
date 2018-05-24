# create requests
import requests as rq
import time


class Camera:
    addr = "http://"
    door_id = 0

    def __init__(self, **kwargs):
        self.addr += kwargs['ip'] + '/'
        door_id = int(kwargs['door_id'])
        self.addr += "?door_id=" + str(door_id)
        self.delay = 0

    def success(self, **kwargs):
        if self.delay < time.time():
            rq.get(self.addr + "&name=" + kwargs["name"])
            self.delay = time.time() + 4  # sec
