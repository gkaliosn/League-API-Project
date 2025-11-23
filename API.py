import urllib.request
import json

headers = {
	  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
	"X-Riot-Token": ""
}

def requestMatches(PUUID , i):
	matchesRequest = urllib.request.Request("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/" + PUUID + "/ids?queueId=1700&start="+ str(i*100)+"&count=100", headers = headers)
	matchesResponse = urllib.request.urlopen(matchesRequest)
	matchesData = matchesResponse.read().decode('utf-8')
	matchesID = json.loads(matchesData)
	return matchesID

def requestMatchData(matchID):
	matchRequest = urllib.request.Request("https://europe.api.riotgames.com/lol/match/v5/matches/"+ matchID, headers=headers)
	matchResponse = urllib.request.urlopen(matchRequest)
	data = matchResponse.read().decode('utf-8')
	matchData = json.loads(data)
	return matchData
