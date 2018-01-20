# -*- coding: utf-8 -*-
from server import Server
import base64
import simplejson as json

serv = Server()
class Models(object):

	"""Generator"""

	def decodeB64(self, text):
		return base64.b64decode(text)

	def encodeB64(self, text):
		return base64.b64encode(text.encode('utf-8'))

	def shortenGoogle(self, url):
		req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyDJmDnUBn5P2ecDw6x8uqiSGeS6fDvi2Y8'
		payload = {'longUrl': url}
		headers = {'content-type': 'application/json'}
		r = serv.postContent(req_url, data=json.dumps(payload), headers=headers)
		resp = json.loads(r.text)
		return resp['id']