import requests,time
import simplejson as json
from server import Server
from models import Models

mod  = Models() 
serv = Server()
class Object(object):

	_time = str(time.time()).split(".")[0]

	def searchResults(self, keywords):
		apiURI      = "http://api.joox.com/web-fcgi-bin//web_search"
		params      = {"callback":"jQuery110007680156477433364_1516238311941","lang":"en","country":"id","type":"0","search_input":keywords,"pn":1,"sin":"0","ein":"29","_":self._time}
		parse_jsonp = serv.getJsonp(apiURI,params=params)

		results = []
		for jsonp in parse_jsonp['itemlist']:
			result = {}
			result['album']     = mod.decodeB64(jsonp['info3'])
			result['artist']    = mod.decodeB64(jsonp['info2'])
			result['playtime']  = jsonp['playtime']
			result['single']    = mod.decodeB64(jsonp['info1'])
			result['songid']    = jsonp['songid']
			results.append(result)
		return results

	def songlyricResult(self, songid):
		URI		= "http://api.joox.com/web-fcgi-bin/web_lyric"
		params  = {"musicid":songid,"lang":"en","country":"id","_":self._time} 
		parse_jsonp = serv.getJsonp(URI,params=params)
		result      = mod.decodeB64(parse_jsonp['lyric'])
		return result

	def songinfoResults(self, songid):
		URI		= "http://api.joox.com/web-fcgi-bin/web_get_songinfo"
		params  = {"songid":songid,"lang":"en","country":"id","from_type":"null","channel_id":"null","_":self._time}
		parse_jsonp = serv.getJsonp(URI,params=params)
		try:
			results = {}
			results['artist']    = parse_jsonp['msinger']
			results['album']     = parse_jsonp['malbum']
			results['duration']  = parse_jsonp['minterval']
			results['lyric']	 = self.songlyricResult(songid=songid)
			results['mp3Url']    = mod.shortenGoogle(parse_jsonp['mp3Url'])
			results['m4aUrl']    = mod.shortenGoogle(parse_jsonp['m4aUrl'])
			results['song']      = parse_jsonp['msong']
			results['thumbnail'] = parse_jsonp['imgSrc']
			return results
		except:
			return parse_jsonp