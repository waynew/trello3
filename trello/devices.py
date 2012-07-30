import json
import requests

class Devices(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get_field(self, field, idDevice):
        resp = requests.get("https://trello.com/1/devices/%s/%s" % (idDevice, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, idDevice, fields=None):
        resp = requests.get("https://trello.com/1/devices/%s/member" % (idDevice), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_field(self, field, idDevice):
        resp = requests.get("https://trello.com/1/devices/%s/member/%s" % (idDevice, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    
