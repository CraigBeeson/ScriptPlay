import tkinter
import Defs
from Classes import Item
class InvMenu:
	def __init__(self,gui,menu):
		self.gui = gui
		self.menu = menu
	
	def setInvMenu(self):
		#sets inventory options based on item type
		#sets equipment submenu
		equipSub = tkinter.Menu(self.menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		self.menu.add_cascade(label='Equipment',menu=equipSub)
		self.equipSubLoop(equipSub)
		#sets key items submenu
		keySub = tkinter.Menu(self.menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		self.menu.add_cascade(label='Key Items',menu=keySub)
		self.keySubLoop(keySub)
		#sets consumable submenu
		conSub = tkinter.Menu(self.menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		self.menu.add_cascade(label="Consumables",menu=conSub)
		self.conSubLoop(conSub)
		#sets resource submenu
		resSub = tkinter.Menu(self.menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		self.menu.add_cascade(label="Resources",menu=resSub)
		self.resSubLoop(resSub)

	def resetInvMenu(self):
		for i in Defs.items.keys():
			self.menu.delete(0)
		self.setInvMenu()

	def equipSubLoop(self,menu):
		for k in Defs.items["equipment"].keys():
			tMenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
			menu.add_cascade(label=k,menu=tMenu)
			for i in self.gui.player.viewInventory():
				if i[0] in Defs.items["equipment"][k].keys():
					tempMenu = tkinter.Menu(tMenu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
					tMenu.add_cascade(label=i[0] + " X " + str(i[1]),menu=tempMenu)
					self.equipOpts(tempMenu,Item.Item(i[0],i[1]))

	def keySubLoop(self,menu):
		for k in Defs.items["key items"].keys():
			tMenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
			menu.add_cascade(label=k,menu=tMenu)
			for i in self.gui.player.viewInventory():
				if i[0] in Defs.items["key items"][k].keys():
					tempMenu = tkinter.Menu(tMenu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
					tMenu.add_cascade(label=i[0] + " X " + str(i[1]),menu=tempMenu)
					self.keyOpts(tempMenu,Item.Item(i[0],i[1]))

	def keyOpts(self,menu,item):			
		menu.add_command(label="Examine",command=lambda: self.examine(item))

	def conSubLoop(self,menu):
		for k in Defs.items["consumables"].keys():
			tMenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
			menu.add_cascade(label=k,menu=tMenu)
			for i in self.gui.player.viewInventory():
				if i[0] in Defs.items["consumables"][k].keys():
					tempMenu = tkinter.Menu(tMenu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
					tMenu.add_cascade(label=i[0] + " X " + str(i[1]),menu=tempMenu)
					self.conOpts(tempMenu,Item.Item(i[0],i[1]))

	def resSubLoop(self,menu):
		for k in Defs.items["resources"].keys():
			tMenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
			menu.add_cascade(label=k,menu=tMenu)
			for i in self.gui.player.viewInventory():
				if i[0] in Defs.items["resources"][k].keys():
					tempMenu = tkinter.Menu(tMenu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
					tMenu.add_cascade(label=i[0] + " X " + str(i[1]),menu=tempMenu)
					self.resOpts(tempMenu,Item.Item(i[0],i[1]))

	def resOpts(self,menu,item):
		menu.add_command(label="Examine",command=lambda: self.examine(item))

	def conOpts(self,menu,item):
		if item.name in Defs.items["consumables"]["restoratives"]:
			eMenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
			menu.add_cascade(label="Use",menu = eMenu)
			eMenu.add_command(label=self.gui.player.viewParty()[0].name,command=lambda: self.gui.player.use(self.gui.player.viewParty()[0].name,item))
			eMenu.add_command(label=self.gui.player.viewParty()[1].name,command=lambda: self.gui.player.use(self.gui.player.viewParty()[1].name,item))
			eMenu.add_command(label=self.gui.player.viewParty()[2].name,command=lambda: self.gui.player.use(self.gui.player.viewParty()[2].name,item))
			eMenu.add_command(label=self.gui.player.viewParty()[3].name,command=lambda: self.gui.player.use(self.gui.player.viewParty()[3].name,item))
			menu.add_command(label="Examine",command=lambda: self.examine(item))
		elif item.name in Defs.items["consumables"]["offensive"] and self.gui.viewCombat == True:
			pass
		sMenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		menu.add_cascade(label="Sell",menu=sMenu)
		sMenu.add_command(label="X 1",command=lambda: self.gui.player.sell(item,1))
		if item.amount >= 5:
			sMenu.add_command(label="X 5",command=lambda: self.sell(item,5))
		if item.amount >= 10:
			sMenu.add_command(label="X 10",command=lambda: self.sell(item,10))

	def equipOpts(self,menu,item):
		eMenu = tkinter.Menu(self.menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		menu.add_cascade(label="Equip",menu = eMenu)
		eMenu.add_command(label=self.gui.player.viewParty()[0].name,command=lambda: self.equip(self.gui.player.viewParty()[0].name,item))
		eMenu.add_command(label=self.gui.player.viewParty()[1].name,command=lambda: self.equip(self.gui.player.viewParty()[1].name,item))
		eMenu.add_command(label=self.gui.player.viewParty()[2].name,command=lambda: self.equip(self.gui.player.viewParty()[2].name,item))
		eMenu.add_command(label=self.gui.player.viewParty()[3].name,command=lambda: self.equip(self.gui.player.viewParty()[3].name,item))
		menu.add_command(label="Examine",command=lambda: self.examine(item))
		menu.add_command(label="Discard",command=lambda: self.gui.player.discard(item))
		sMenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		menu.add_cascade(label="Sell",menu=sMenu)
		sMenu.add_command(label="X 1",command=lambda: self.gui.player.sell(item,1))
		if item.amount >= 5:
			sMenu.add_command(label="X 5",command=lambda: self.gui.player.sell(item,5))
		if item.amount >= 10:
			sMenu.add_command(label="X 10",command=lambda: self.gui.player.sell(item,10))

	def use(gui,character,item):
		if item.name in Defs.items["consumables"]["restoratives"]:
			restoreUse(gui,character,item)
		elif item.name in Defs.items["consumables"]["offensive"]:
			offensiveUse(gui,item)

	def restoreUse(gui,character,item):
		usage = item.info["use"]
		if usage["hp"]:
			character.addHP(usage["hp"])
			gui.updateOutputList(character.name + " restored " + str(usage["hp"]) + " hitpoints.")
		self.removeInvItem(gui,item.name,1)
		self.resetInvMenu(gui)

	def examine(self,item):
		self.gui.updateOutputList(item.info["desc"])
		if "stats" in item.info.keys():
			self.gui.updateOutputList("Stats")
			for l in item.info["stats"].keys():
				self.gui.updateOutputList("          " + l + " : " + str(item.info["stats"][l]))

	def equip(self,character,item):
		self.gui.player.equipItem(character,item)
		self.resetInvMenu()