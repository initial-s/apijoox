# -*- coding: utf-8 -*-
import json,requests

class Server(object):

	_session	= requests.session()


	def getJsonp(self, url,params=None):
		r = self._session.get(url,params=params).text
		r = r.split("(")[1].strip("\n)")
		jsonp = json.loads(r)
		return jsonp

	def getJson(self, url):
		 json.loads(self._session.get(url).text)

	def getContent(self, url, headers=None):
		return self._session.get(url,headers=headers, stream=True)

	def postContent(self, url, data=None, files=None, headers=None):
		return self._session.post(url, headers=headers, data=data, files=files)