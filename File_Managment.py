import json

#List of Friend Names
Names = ["Me"]

def cleanFiles():
	for Name in Names:
		with open(Name + "LOG.json", 'w') as file:
			file.write("[")

def initialize_files():
	for Name in Names:
		with open(Name + "LOG.json", 'w') as file:
			file.write("[")

def initialize_visited_matches():
	try:
		with open('viewed_games.json', 'r') as file:
			visited_matches = json.load(file)
	except:
		visited_matches = []
	return visited_matches

def save_log(friend , player):
	with open(friend.name + "LOG.json", 'a') as file:
		json.dump(player, file, indent=2)
		file.write(",")

def save_all_friends(friends):
	for friend in friends:
		friend.save_friend_to_file()	


def save_viseted_matches(visited_match_list):
	with open('viewed_games.json', 'w') as file:
		json.dump(visited_match_list,file,indent=2)

