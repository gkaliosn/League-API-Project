import json
import time
from Player import *
from File_Managment import *
from API import *


#PUUIDs of Players
PUUIDs = ["Me"]

visited_matches = initialize_visited_matches()
players = initialize_players(PUUIDs , Names)

i=0
while i<13: # until we get 1300 games
	for PUUID in PUUIDs:
		matchIDs = requestMatches(PUUID , i)
		print(PUUID + "  " + str(i))
		time.sleep(0.2) #sleep for the limit of the API
		for matchID in matchIDs:
			print(matchID)

			if matchID not in visited_matches:
				matchData = requestMatchData(matchID)
				time.sleep(1.5) #sleep for the limit of the API

				visited_matches.append(matchID)
				save_viseted_matches(visited_matches)

				if matchData['info']['gameMode']=="CHERRY":
					
					for player in matchData['info']['participants']:
						player_puuid = player['puuid']
						if player_puuid in PUUIDs:
							del player['challenges'], player['perks'] , player['missions'] #Big chunks, delete to save space and readability

							for player in players:
								if(player.puuid==player_puuid):
									save_log(player, player)
					
	i+=1
