import json
import requests

class API(object):

	def __init__(self):
		f = open("conf.json")
		j = json.loads(f.read())
		f.close()

		self.addr = j['api']


	def loadServer(self, name):
		r = requests.post(self.addr + "getvm", data=name)
		req = json.loads(r.text)

		return req