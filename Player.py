import json
from Items import html_to_id_name_dict_simple

#List of Players Names and PUUIDS
Names = ["Me"]
PUUIDs = ["bPn3nAlHpefjofAh5y2VShA5dp2CxI7ia3O1qUv7uBq373Pc0YwGAe_SdhYdWNu6Zw6tnSgoEi-97Q"]



class Player:
	def __init__(self , puuid , name):
		self.puuid = puuid
		self.name = name
		self.matches = 0
		self.kills = 0
		self.assists = 0
		self.deaths = 0
		self.dmgDealt  = 0
		self.dmgTaken  = 0
		self.dmgHealed = 0
		self.ccTime = 0
		self.place = 0
		self.wins = 0
		self.statgames = 0
		self.spellCasts = 0
		self.pings = 0
		self.crit = 0
		self.items = {}
		self.augmentPicks = {}
		self.augmentWins = {}
		self.augmentWinrates= {}
		self.champions = {}

	def add_champion(self , championID):
		if championID in self.champions:
			self.champions[championID]+=1
		else:
			self.champions[championID]=1


	def add_items(self , stat):
		for i in range(0,6):
			item_key = 'item' + str(i)	
			item=stat[item_key]
			if item !=0:
				if item in self.items:
					self.items[item]+=1
				else:
					self.items[item]=1

	
	def add_augment(self, stat):
		for i in range(1,7):
			augment_key ='playerAugment'+ str(i)

			if augment_key in stat:
				augment = stat[augment_key]

				if augment != 0:

					if augment in self.augmentPicks:
						self.augmentPicks[augment] += 1
					else:
						self.augmentPicks[augment] = 1
					

					if stat['placement'] == 1:
						if augment in self.augmentWins:
							self.augmentWins[augment] += 1
						else:
							self.augmentWins[augment] = 1

	def print(self , championList):
		return f"""
=== PLAYER INFO ===
Name: {self.name}

=== BASIC STATS ===
Matches: {self.matches} | Wins: {self.wins} | Win Rate: {(self.wins/self.matches*100) if self.matches > 0 else 0:.1f}%
K/D/A: {self.kills}/{self.deaths}/{self.assists} , AVGs: {self.kills/self.matches:.2f}/{self.deaths/self.matches:.2f}/{self.assists/self.matches:.2f}  | KDA: {((self.kills + self.assists) / self.deaths):.2f}

=== COMBAT STATS ===
Damage Dealt: {self.dmgDealt:,} || AVGs: {self.dmgDealt/self.matches:.2f}
Damage Taken: {self.dmgTaken:,} || AVGs: {self.dmgTaken/self.matches:.2f}
Damage Healed: {self.dmgHealed:,} || AVGs: {self.dmgHealed/self.matches:.2f}
CC Time: {self.ccTime} || AVGs: {self.ccTime/self.matches:.2f}
Biggest Critical Strike: {self.crit}

=== GAME ACTIONS ===
Spell Casts: {self.spellCasts} || Per Game: {self.spellCasts/self.matches:.1f}
Pings: {self.pings} || Per Game: {self.pings/self.matches:.1f}
Average Place: {self.place/self.matches:.3f} 

=== COLLECTIONS ===
Items Collected: {len(self.items)} || Most Picked: {list(self.items.items())[:5]}
Augments Picked: {len(self.augmentPicks)} || Most Picked: {list(self.augmentPicks.items())[:5]}
Augments Wins: {len(self.augmentWins)} || Most Wins: {list(self.augmentWins.items())[:5]}
Augments Winrates {list(self.augmentWinrates.items())[:5]}

Champions Played: {len(self.champions)} || Most Picked: {list(self.champions.items())[:5]}
Champions Not Played: {list(set(championList) - set(self.champions.keys()))}
"""

def initialize_players(PUUIDs , Names):
	players = []
	for i in range(len(Names)):
		player = Player(PUUIDs[i] , Names[i])
		players.append(player)
	return players
