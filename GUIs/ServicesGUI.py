import tkinter
import Defs
import time
import threading
import os
import pickle
import importlib
from importlib import util
import sys

autoSaveThread = None
autoState = None
scriptStates = None

def main(gui,menu):
	global autoState,active
	global scriptStates
	scriptStates = [threading.Event(),threading.Event(),threading.Event(),threading.Event()]
	autoState = tkinter.IntVar(value=1)
	menu.add_checkbutton(label='AutoSave', variable=autoState, onvalue=1, offvalue=0,
selectcolor=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	autoSaveThread = saveThread(gui.player,autoState)
	autoSaveThread.start()
	scriptMenu(gui,menu)

def scriptMenu(gui,menu):
	for i in scriptStates:
		i.set()
	scriptList = []
	with os.scandir(os.getcwd() + "\\Scripts\\") as Scripts:
		for script in Scripts:
			if script.name.endswith(".py"):
				scriptList.append(script.name)
	scriptSub = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
	script0 = tkinter.Menu(scriptSub,tearoff=False)
	script1 = tkinter.Menu(scriptSub,tearoff=False)
	script2 = tkinter.Menu(scriptSub,tearoff=False)
	script3 = tkinter.Menu(scriptSub,tearoff=False)
	scriptSub.add_cascade(label=gui.player.viewParty()[0].name + " script",menu=script0)
	scriptSub.add_cascade(label=gui.player.viewParty()[1].name + " script",menu=script1)
	scriptSub.add_cascade(label=gui.player.viewParty()[2].name + " script",menu=script2)
	scriptSub.add_cascade(label=gui.player.viewParty()[3].name + " script",menu=script3)
	scriptSub.add_command(label="Disable Scripts", command=disableScripts,
foreground=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	scriptSub.add_command(label="Reload Scripts", command=lambda: scriptReload(scriptSub,gui,menu),
foreground=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	for i in scriptList:
		script0.add_command(label=i,command=lambda script=i: assignScript(gui,gui.player,gui.player.viewParty()[0].name,0,script),
foreground=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
		script1.add_command(label=i,command=lambda script=i: assignScript(gui,gui.player,gui.player.viewParty()[1].name,1,script),
foreground=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
		script2.add_command(label=i,command=lambda script=i: assignScript(gui,gui.player,gui.player.viewParty()[2].name,2,script),
foreground=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
		script3.add_command(label=i,command=lambda script=i: assignScript(gui,gui.player,gui.player.viewParty()[3].name,3,script),
foreground=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	menu.add_cascade(label="Party Scripts",menu=scriptSub)

def scriptReload(subMenu,gui,menu):
	subMenu.destroy()
	scriptMenu(gui,menu)
	

class saveThread(threading.Thread):
	def __init__(self,player,active):
		threading.Thread.__init__(self)
		self.player = player
		self.active = active
		self.daemon = True
	def run(self):
		save(self.player,self.active)

class playThread(threading.Thread):
	def __init__(self,player,name,state,script):
		threading.Thread.__init__(self)
		self.player = player
		self.state = state
		self.script = script
		self.daemon = True
		self.name = name
	def run(self):
		self.script.main(self.player,self.name,self.state)

def disableScripts():
	global scriptStates
	for i in range(0,len(scriptStates)):
		scriptStates[i].clear()

def assignScript(gui,player,name,state,script):
	global scriptStates
	scriptStates[state].clear()
	scriptStates[state] = threading.Event()
	scriptStates[state].set()
	try:
		spec = util.spec_from_file_location("module.name",os.getcwd()+"/Scripts/" + script)
		scriptMod = util.module_from_spec(spec)
		sys.modules["module.name"] = scriptMod
		spec.loader.exec_module(scriptMod)
		playThread(player,name,scriptStates[state],scriptMod).start()
	except:
		gui.updateOutputList("An error occurred loading the script.")

def save(player,active):
	while True:
		if active.get():
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
		time.sleep(15)