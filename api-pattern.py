# create requests
import requests as rq

class Camera:
      addr = "http://"
      door_id = 0
      def __init__(self, **kwargs):
            addr += kwargs['ip'] + '/'
            door_id = int(kwargs['door_id'])
            addr += "?door_id=" + str(door_id)
      
      def success(self, **kwargs):
            rq.get(addr + "&name="  + kwargs["name"])
