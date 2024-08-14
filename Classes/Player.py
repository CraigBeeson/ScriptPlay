import Defs
import Classes
import GUIs
import copy
import threading
import Utility
import math
import random

class Player():
	def __init__(self,gui):
		self.__inventory=[]
		self.__gui = gui
		self.__party = [Classes.Character.Character("Craig"),Classes.Character.Character("Dustin"),Classes.Character.Character("Jimmy"),Classes.Character.Character("Jonny")]
		self.__gold = 100
		self.__CDScript = threading.Thread(target=Utility.GameTick.main,args=([self.__party]),daemon=True).start()
	
	def viewInventory(self):
		return copy.deepcopy(self.__inventory)
	
	def viewParty(self):
		return copy.deepcopy(self.__party)
	
	def __addInvItem(self,item,amount):
		if item == "":
			return
		for i in self.__inventory:
			if item == i[0]:
				i[1]+=amount
				self.__gui.updateOutputList(str(amount) + " x " + item + " added to inventory.")
				return
		self.__inventory.append([item,amount])
		self.__gui.updateOutputList(str(amount) + " x " + item + " added to inventory.")

	def __addResItem(self,item):
		for i in self.__inventory:
			if item == i[0]:
				i[1] += 1
				return
		self.__inventory.append([item,1])

	def __removeInvItem(self,item,amount):
		for i in self.__inventory:
			if item == i[0]:
				i[1]-=amount
				self.__gui.updateOutputList(str(amount) + " x " + item + " removed from inventory.")
				if i[1] == 0:
					self.__inventory.remove(i)
				return
	def equipItem(self,selection,item):
		character = self.__validChar(selection,busy=False)
		try:
			self.__addInvItem(character.equipItem(self.__gui,self,item),1)
			self.__removeInvItem(item.name,1)
		except:
			self.__gui.updateOutputList("Item not found.")
	
	def mine(self,name):
		character = self.__validChar(name)
		if character:
			self.busy(character,"mining")
			resList = []
			for i in Defs.items["resources"]["ores"].keys():
				if Defs.items["resources"]["ores"][i]["level"] <= character.skills["mining"]["level"]:
					resList.append(i)
			res = random.choice(resList)
			self.__addResItem(res)
			self.__addSkillXp(character,"mining",Defs.items["resources"]["ores"][res]["xp"])
			self.__gui.updateOutputList(character.name + " has mined " + res + ".")
			self.__gui.invMenu.resetInvMenu()
	
	def fish(self,name):
		character = self.__validChar(name)
		if character:
			self.busy(character,"fishing")
			resList = []
			for i in Defs.items["resources"]["fish"].keys():
				if Defs.items["resources"]["fish"][i]["level"] <= character.skills["fishing"]["level"]:
					resList.append(i)
			res = random.choice(resList)
			self.__addResItem(res)
			self.__addSkillXp(character,"fishing",Defs.items["resources"]["fish"][res]["xp"])
			self.__gui.updateOutputList(character.name + " caught a " + res + ".")
			self.__gui.invMenu.resetInvMenu()
	
	def forage(self,name):
		character = self.__validChar(name)
		if character:
			self.busy(character,"foraging")
			resList = []
			for i in Defs.items["resources"]["plants"].keys():
				if Defs.items["resources"]["plants"][i]["level"] <= character.skills["foraging"]["level"]:
					resList.append(i)
			res = random.choice(resList)
			self.__addResItem(res)
			self.__addSkillXp(character,"foraging",Defs.items["resources"]["plants"][res]["xp"])
			self.__gui.updateOutputList(character.name + " picked some " + res + ".")
			self.__gui.invMenu.resetInvMenu()
	
	def hunt(self,name):
		character = self.__validChar(name)
		if character:
			self.busy(character,"hunting")
			resList = []
			for i in Defs.items["resources"]["animals"].keys():
				if Defs.items["resources"]["animals"][i]["level"] <= character.skills["hunting"]["level"]:
					resList.append(i)
			res = random.choice(resList)
			self.__addResItem(res)
			self.__addSkillXp(character,"hunting",Defs.items["resources"]["animals"][res]["xp"])
			self.__gui.updateOutputList(character.name + " caught a " + res + ".")
			self.__gui.invMenu.resetInvMenu()
	
	def __addSkillXp(self,character,skill,xp):
		character.skills[skill]["xp"] += xp
		if character.skills[skill]["level"] != 99:
			while (character.skills[skill]["xpToLevel"] <= character.skills[skill]["xp"]):
				character.skills[skill]["level"] += 1
				character.skills[skill]["xpToLevel"] += round(character.skills[skill]["xpToLevel"] * 1.1,0)
	
	def animalProcessing(self):
		pass
	
	def busy(self,character,skill):
		character.cooldown = 60.0 - math.pow(60, (character.skills[skill]["level"] * character.stats["wisdom"])/10000.0)
		character.busy = True
	
	def discard(self,item):
		try:
			self.__inventory.remove([item.name,item.amount])
			self.__gui.updateOutputList(str(item.amount) + " " + item.name + " discarded.")
			self.__gui.invMenu.resetInvMenu()
		except:
			self.__gui.updateOutputList("You do not have this item to discard.")
	
	def sell(self,item,count):
		hasItem = self.__hasItem(item.name,count)
		if not hasItem:
			self.__gui.updateOutputList("You do not have " + str(count) + " " + str(item.name) + " to sell.")
			return
		self.__removeInvItem(item.name,count)
		self.__gold += item.info["value"] * count
		self.__gui.updateOutputList(str(item.info["value"] * count) + " coin's added to pouch.")
		self.__gui.invMenu.resetInvMenu()
	
	def __hasItem(self,item,count):
		for i in self.__inventory:
			if (i[0] == item) and (i[1] >= count):
				return True
		return False
	
	def use(self,character,item):
		hasItem = self.__hasItem(item.name,1)
		selection = self.__validChar(character,busy=False)
		if hasItem:
			if item.name in Defs.items["consumables"]["restoratives"]:
				self.__restoreUse(selection,item)
			elif item.name in Defs.items["consumables"]["offensive"]:
				self.__offensiveUse(item)
		else:
			self.__gui.updateOutputList("You do not have " + str(item.name))
	
	def __restoreUse(self,character,item):
		usage = item.info["use"]
		if usage["hp"]:
			character.addHP(usage["hp"])
			self.__gui.updateOutputList(character.name + " restored " + str(usage["hp"]) + " hitpoints.")
		self.__removeInvItem(item.name,1)
		self.__gui.invMenu.resetInvMenu()
	
	def __offensiveUse(gui,item):
		gui.updateOutputList("You can only use this item during combat.")
	
	def __addHP(self,selection,amount):
		selection.addHP(amount)
	
	def __validChar(self,name,busy=True):
		character = None
		for i in range(0,len(self.__party)):
			if self.__party[i].name == name:
				character = self.__party[i]
		if character == None:
			self.__gui.updateOutputList("Cannot find character named '" + name + "'.")
			return character
		if character.busy and busy:
			self.__gui.updateOutputList(character.name + " is busy.")
			return None
		return character