import tkinter
import os
import pickle

def ToolMenu(gui,menu):
	menu.add_command(label="Save",command = lambda: save(gui.player))

def save(player):
	playerDict = {}
	playerDict["inventory"] = player.viewInventory()
	playerDict["gold"] = player.getGold()
	characters = player.viewParty()
	playerDict["characters"] = {}
	for i in characters:
		playerDict["characters"][i.name] = {}
		playerDict["characters"][i.name]["equipment"] = i.viewEquipment()
		playerDict["characters"][i.name]["stats"] = i.stats
		playerDict["characters"][i.name]["skills"] = i.skills
		playerDict["characters"][i.name]["hp"] = i.hp
	with open(os.getcwd() + "/Players/" + player.getName() + ".pickle", "wb") as file:
		pickle.dump(playerDict,file)
		file.close()