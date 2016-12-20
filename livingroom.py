from pprint import pprint
import urllib
import json
kodi_ip = "benpi2.home:80"
def get_kodi_info(kodi_ip):


	kodi_addr = "http://"+kodi_ip + "/jsonrpc?request="
	
	def getData(request):
		addr = kodi_addr + request 
		response = urllib.urlopen(addr)

		jsonData = json.loads(response.read())
		#print addr
		#pprint(jsonData)
		return jsonData;
		
	nowPlayingUrl =  '{"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}'
	nowPlayingType = getData(nowPlayingUrl)

	try:
		if (nowPlayingType["result"][0]["type"]=="video"):
			playType = "video"
		else:
			playType = "unknown"
	except:
		playType = "unknown"
	


	if playType == "video":
		nowPlaying = getData('{"jsonrpc": "2.0", "method": "Player.GetItem", "params": { "properties": ["title", "album", "artist", "season", "episode", "duration", "showtitle", "tvshowid", "thumbnail", "file", "fanart", "streamdetails"], "playerid": 1 }, "id": "VideoGetItem"}')
		
		videoType = nowPlaying['result']['item']['type']

		if videoType=="episode":
			showTitle = nowPlaying['result']['item']['showtitle']
 
			title = nowPlaying['result']['item']['title']
			thumbnail = nowPlaying['result']['item']['thumbnail']

			return {'showTitle':showTitle, 'title':title, 'thumbnail':thumbnail}

	else:
		return {'status':'None'}


kodi_info = get_kodi_info(kodi_ip)

pprint(kodi_info)

	
