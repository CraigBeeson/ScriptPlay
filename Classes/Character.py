import Defs
import GUIs
import Classes

class Character():
	def __init__(self,name):
		self.name=name
		self.cooldown = 0
		self.busy = False
		self.__equipment= {
			"main-hand" : "nothing",
			"off-hand" : "nothing",
			"head" : "nothing",
			"chest" : "nothing",
			"legs" : "nothing",
		}
		self.stats = {
			"strength" : 1,
			"dexterity" : 1,
			"wisdom" : 1,
			"vitality" : 1,
			"hp" : 10,
			"attack" : 0,
			"armor" : 0,
		}
		self.skills = {
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
		}
		self.hp = self.stats["hp"]
	
	def recvDmg(self,dmg):
		finalDmg = float(dmg - (self.stats["armor"] + self.stats["vitality"]))
		if finalDmg >= .01:
			self.hp -= round(finalDmg,2)
	
	def addHP(self,amount):
		self.hp += amount
		if self.hp > self.stats["hp"]:
			self.hp = self.stats["hp"]
	
	def viewStats(self):
		return self.stats
	
	def viewEquipment(self):
		return self.__equipment
	
	def equipItem(self,gui,player,item):
		hasItem = False
		for i in player.viewInventory():
			if i[0] == item.name:
				hasItem = True
		if hasItem:
			temp = ""
			for k in Defs.items["equipment"].keys():
				if item.name in Defs.items["equipment"][k].keys():
					slot = k
					if self.viewEquipment()[k] != "nothing":
						temp = Classes.Item.Item(self.viewEquipment()[k])
						for i in temp.info["stats"].keys():
							self.stats[i] -= temp.info["stats"][i]
			self.__equipment[slot] = item.name
			for i in item.info["stats"].keys():
				self.stats[i] += item.info["stats"][i]
			gui.updateOutputList(self.name + " has equipped " + item.name + ".")
			if temp != "":
				return temp.name
			else:
				return ""