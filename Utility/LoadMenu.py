import tkinter
import Defs
import os
from Classes import Player,Character
import pickle

class PlayerConfig:
	def __init__(self,gui):
		self.player = None
		self.loadMenu = tkinter.Toplevel()
		self.loadMenu.title = "Load Player"
		self.loadMenu.config(width = 300,height = 200,bg=Defs.bg)
		playerName = tkinter.Entry(self.loadMenu,width = 25,bg=Defs.bg,fg=Defs.fg,insertbackground=Defs.fg)
		playerName.insert(0,"Enter Name")
		playerName.pack()
		loadButton = tkinter.Button(self.loadMenu,text="Load",command=lambda: handleText(gui,playerName.get(),self.loadMenu),bg=Defs.bg,fg=Defs.fg,activebackground=Defs.active)
		loadButton.pack()
		gui.root.wait_window(self.loadMenu)

def handleText(gui,playerName,window):
	try:
		loadPlayer(gui,playerName,window)
	except:
		newPlayerMenu(gui,playerName,window)

def loadPlayer(gui,playerName,window):
	playerDict = None
	with open(os.getcwd() + "/Players/" + playerName + ".pickle","rb") as file:
		playerDict = pickle.load(file)
		file.close()
	characters = []
	for i in playerDict["characters"].keys():
		characters.append(Character.Character(i,playerDict["characters"][i]))
	gui.player = Player.Player(gui,playerName,characters,playerDict["gold"],playerDict["inventory"])
	window.destroy()

def savePlayer(player):
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

def newPlayerMenu(gui,playerName,window):
	for i in window.winfo_children():
		i.destroy()
	char1 = tkinter.Entry(window,width=25,bg=Defs.bg,fg=Defs.fg,insertbackground=Defs.fg)
	char1.insert(0,"Character 1 Name")
	char1.pack()
	char2 = tkinter.Entry(window,width=25,bg=Defs.bg,fg=Defs.fg,insertbackground=Defs.fg)
	char2.insert(0,"Character 2 Name")
	char2.pack()
	char3 = tkinter.Entry(window,width=25,bg=Defs.bg,fg=Defs.fg,insertbackground=Defs.fg)
	char3.insert(0,"Character 3 Name")
	char3.pack()
	char4 = tkinter.Entry(window,width=25,bg=Defs.bg,fg=Defs.fg,insertbackground=Defs.fg)
	char4.insert(0,"Character 4 Name")
	char4.pack()
	createButton = tkinter.Button(window,text="Create Game",command=lambda: newPlayer(gui,playerName,[char1.get(),char2.get(),char3.get(),char4.get()],window),bg=Defs.bg,fg=Defs.fg,activebackground=Defs.active)
	createButton.pack()

def newPlayer(gui,playerName,charNames,window):
	inv = []
	gold = 100
	characters = [Character.Character(charNames[0]),Character.Character(charNames[1]),Character.Character(charNames[2]),Character.Character(charNames[3])]
	gui.player = Player.Player(gui,playerName,characters,gold,inv)
	savePlayer(gui.player)
	window.destroy()

try:
	os.mkdir(os.getcwd()+"/Players")
except:
	pass
"""
	characters = {
		name1 : {
			"equipment" : {
				"main-hand" : "nothing",
				"off-hand" : "nothing",
				"head" : "nothing",
				"chest" : "nothing",
				"legs" : "nothing",
			},
			"hp" : 10,
			"stats" : {
				"strength" : 1,
				"dexterity" : 1,
				"wisdom" : 1,
				"vitality" : 1,
				"hp" : 10,
				"attack" : 0,
				"armor" : 0,
			},
			"skills" : {
				"mining" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"fishing" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"hunting" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"foraging" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
			},
		},
		name2 : {
			"equipment" : {
				"main-hand" : "nothing",
				"off-hand" : "nothing",
				"head" : "nothing",
				"chest" : "nothing",
				"legs" : "nothing",
			},
			"hp" : 10,
			"stats" : {
				"strength" : 1,
				"dexterity" : 1,
				"wisdom" : 1,
				"vitality" : 1,
				"hp" : 10,
				"attack" : 0,
				"armor" : 0,
			},
			"skills" : {
				"mining" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"fishing" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"hunting" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"foraging" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
			},
		},
		name3 : {
			"equipment" : {
				"main-hand" : "nothing",
				"off-hand" : "nothing",
				"head" : "nothing",
				"chest" : "nothing",
				"legs" : "nothing",
			},
			"hp" : 10,
			"stats" : {
				"strength" : 1,
				"dexterity" : 1,
				"wisdom" : 1,
				"vitality" : 1,
				"hp" : 10,
				"attack" : 0,
				"armor" : 0,
			},
			"skills" : {
				"mining" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"fishing" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"hunting" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"foraging" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
			},
		},
		name4 : {
			"equipment" : {
				"main-hand" : "nothing",
				"off-hand" : "nothing",
				"head" : "nothing",
				"chest" : "nothing",
				"legs" : "nothing",
			},
			"hp" : 10,
			"stats" : {
				"strength" : 1,
				"dexterity" : 1,
				"wisdom" : 1,
				"vitality" : 1,
				"hp" : 10,
				"attack" : 0,
				"armor" : 0,
			},
			"skills" : {
				"mining" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"fishing" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"hunting" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
				"foraging" : {
					"level" : 1,
					"xp" : 0,
					"xpToLevel" : 83,
				},
			},
		},
	}
"""