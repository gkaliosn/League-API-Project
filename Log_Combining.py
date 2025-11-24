from Player import *
from Game import *
from Items import *
from Augments import *
from collections import Counter

def sumSpellCasts(stat):
	return stat['spell1Casts'] + stat['spell2Casts'] + stat['spell3Casts'] + stat['spell4Casts']


def sumPings(stat):
    total_pings = 0
    for key, value in stat.items():
        if key.endswith('Pings'):
            total_pings += value
    return total_pings


def update_player(player , stat):
	player.matches+=1
	player.kills+= stat['kills']
	player.deaths += stat['deaths']
	player.assists += stat['assists']
	player.dmgDealt += stat['totalDamageDealtToChampions']
	player.dmgHealed += stat['totalUnitsHealed']
	player.dmgTaken += stat['totalDamageTaken']
	player.place += stat['placement']
	player.ccTime += stat['totalTimeCCDealt']
	player.add_champion(stat['championName'])
	player.pings += sumPings(stat)
	player.spellCasts += sumSpellCasts(stat)
	player.add_augment(stat)
	player.add_items(stat)
	if player.crit < stat['largestCriticalStrike']:
		player.crit = stat['largestCriticalStrike']
	if stat['placement']==1:
		player.wins+=1
	if stat['itemsPurchased']<2:
		player.statgames+=1


def update_game(game, player, stat):
	if game.minDMG > stat['totalDamageDealtToChampions'] and stat['totalDamageDealtToChampions']!=0:
		game.minDMG = stat['totalDamageDealtToChampions']
		game.minDMGH = player.name

	if game.maxDMG < stat['totalDamageDealtToChampions']:
		game.maxDMG = stat['totalDamageDealtToChampions']
		game.maxDMGH = player.name

	if game.mostDeaths < stat['deaths']:
		game.mostDeaths = stat['deaths']
		game.mostDeathsH = player.name

	if game.leastDeaths > stat['deaths']:
		game.leastDeaths = stat['deaths']
		game.leastDeathsH = player.name

	if game.mostKills < stat['kills']:
		game.mostKills = stat['kills']
		game.mostKillsH = player.name

	if game.mostDMGTaken < stat['totalDamageTaken']:
		game.mostDMGTaken = stat['totalDamageTaken']
		game.mostDMGTakenH = player.name

	if game.mostHeal < stat['totalHeal']:
		game.mostHeal = stat['totalHeal']
		game.mostHealH = player.name

	if game.mostCC < stat['timeCCingOthers']:
		game.mostCC = stat['timeCCingOthers']
		game.mostCCH = player.name

	if game.maxCrit < stat['largestCriticalStrike']:
		game.maxCrit = stat['largestCriticalStrike']
		game.maxCritH = player.name

	spellCasts = sumSpellCasts(stat)
	if game.mostSpellCasts < spellCasts:
		game.mostSpellCasts = spellCasts
		game.mostSpellCastsH = player.name

	pings = sumPings(stat)
	if game.maxPings < pings:
		game.maxPings = pings
		game.maxPingsH = player.name

	


players = initialize_players(PUUIDs , Names)
game = Game() 
item_dict = html_to_id_name_dict_simple(htmlcontent)
augment_dict = getAugDict()

for player in players:

	filename = player.name + 'LOG.json'

	with open (filename, 'r') as file: 
		stats = json.load(file)

		for stat in stats:
			update_player(player, stat)
			update_game(game, player, stat)

	player.augmentWinrates = {
	augment: round((player.augmentWins.get(augment, 0) / player.augmentPicks[augment]) * 100 ,2)
	for augment in player.augmentPicks 
	}

	player.champions = dict(sorted(player.champions.items(), key=lambda item: item[1], reverse=True))
	player.items = dict(sorted(player.items.items(), key=lambda item: item[1], reverse=True))
	player.augmentPicks = dict(sorted(player.augmentPicks.items(), key=lambda item: item[1], reverse=True))
	player.augmentWins = dict(sorted(player.augmentWins.items(), key=lambda item: item[1], reverse=True))
	player.augmentWinrates = dict(sorted(player.augmentWinrates.items(), key=lambda item: item[1], reverse=True))

	player.items = {item_dict[id]: player.items[id] for id in player.items if id in item_dict}
	player.augmentPicks = {augment_dict[id]: player.augmentPicks[id] for id in player.augmentPicks if id in augment_dict}
	player.augmentWins = {augment_dict[id]: player.augmentWins[id] for id in player.augmentWins if id in augment_dict}
	player.augmentWinrates = {augment_dict[id]: player.augmentWinrates[id] for id in player.augmentWinrates if id in augment_dict}

	game.items = dict(Counter(game.items) + Counter(player.items))
	game.augmentPicks = dict(Counter(game.augmentPicks) + Counter(player.augmentPicks))
	game.augmentWins =dict(Counter(game.augmentWins) + Counter(player.augmentWins))
	game.allChampions = list(Counter(game.allChampions) + Counter(player.champions.keys()))

game.augmentPicks = dict(sorted(game.augmentPicks.items(), key=lambda item: item[1], reverse=True))
game.augmentWins = dict(sorted(game.augmentWins.items(), key=lambda item: item[1], reverse=True))

##############################################################################################
game.augmentWinrates = {
	augment: round((game.augmentWins.get(augment, 0) / game.augmentPicks[augment]) * 100 ,2)
	for augment in game.augmentPicks 
	}

for player in players:
	print(player.print(game.allChampions))
print(str(game))

print("======SEARCH=====  "+ str(Names) +"| Champ , Augm , Item")
Name , Section , Item = "1" , "2", "3"


while not(Name=="" and Section == "" and Item == ""):
	Name = input("Name:")
	Section = input("Section:")
	Item = input("Item:")

	try:
		player = None 
		for player in players:
			if player.name.lower() == Name.lower():
				player = player
				break

		if Section == "Champ":
			if Item=="":
				print(player.champions)
			else:
				print(player.champions[Item])
		if Section == "Augm":
			if Item =="":
				print(player.augmentPicks)
			else:
				print(player.augmentPicks[Item])
		if Section == "Item":
			if Item=="":
				print(player.items)
			else:
				print(player.items[Item])
	except:
		print("Misspelled, try again")
