
class Game:
	def __init__(self):
		self.maxDMG = 0 
		self.minDMG = float('inf')
		self.mostDeaths = 0
		self.leastDeaths = float('inf')
		self.mostKills = 0
		self.mostDMGTaken = 0
		self.mostHeal = 0
		self.mostCC = 0
		self.mostSpellCasts = 0
		self.maxPings = 0
		self.maxCrit = 0
		self.items = {}
		self.augmentPicks = {}
		self.augmentWins = {}
		self.augmentWinrates = {}
		self.allChampions = {}


		self.maxDMGH =  ""
		self.minDMGH = ""
		self.mostDeathsH = ""
		self.leastDeathsH = ""
		self.mostKillsH = ""
		self.mostDMGTakenH = ""
		self.mostHealH = ""
		self.mostCCH = ""
		self.mostSpellCastsH = ""
		self.maxPingsH = ""
		self.maxCritH = ""
	

	def __str__(self):
    	 return f"""
=== GAME RECORDS ===

=== DAMAGE RECORDS ===
Highest Damage Dealt: {self.maxDMG:,}, {self.maxDMGH} 
Lowest Damage Dealt: {self.minDMG:,} , {self.minDMGH} 
Highest Damage Taken: {self.mostDMGTaken:,} , {self.mostDMGTakenH}

=== COMBAT RECORDS ===
Most Kills: {self.mostKills}, {self.mostKillsH}
Most Deaths: {self.mostDeaths}, {self.mostDeathsH}
Least Deaths: {self.leastDeaths}, {self.leastDeathsH}
Most Healing: {self.mostHeal:,}, {self.mostHealH}
Most CC Time: {self.mostCC}, {self.mostCCH}
Biggest Critical Strike: {self.maxCrit},  {self.maxCritH}

=== ACTION RECORDS ===
Most Spell Casts: {self.mostSpellCasts:,}, {self.mostSpellCastsH}
Most Pings: {self.maxPings}, {self.maxPingsH}

=== AUGMENT STATISTICS ===
Total Augments Picked: {len(self.augmentPicks)}
Most Popular Augments: {list(self.augmentPicks.items())[:5]}
Most Winning Augments: {list(self.augmentWins.items())[:5]}
Best Winrates Augments: {list(self.augmentWinrates.items())[:5]}
Most Picked Items: {list(self.items.items())[:5]}
"""