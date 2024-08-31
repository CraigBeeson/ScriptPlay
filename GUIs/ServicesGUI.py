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
script1State = None
script2State = None
script3State = None
script4State = None

def main(gui,menu):
	global autoState,active
	global script1State,script2State,script3State,script4State
	autoState = tkinter.IntVar(value=1)
	menu.add_checkbutton(label='AutoSave', variable=autoState, onvalue=1, offvalue=0,
selectcolor=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	autoSaveThread = saveThread(gui.player,autoState)
	autoSaveThread.start()
	script1State = tkinter.IntVar()
	script2State = tkinter.IntVar()
	script3State = tkinter.IntVar()
	script4State = tkinter.IntVar()
	scriptSub = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
	scriptSub.add_checkbutton(label=gui.player.viewParty()[0].name + " script",
command = lambda: loadScript(gui,gui.player,gui.player.viewParty()[0].name,script1State),variable = script1State,onvalue=1, offvalue=0,
selectcolor=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	scriptSub.add_checkbutton(label=gui.player.viewParty()[1].name + " script",
command = lambda: loadScript(gui,gui.player,gui.player.viewParty()[1].name,script2State),variable = script2State,onvalue=1, offvalue=0,
selectcolor=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	scriptSub.add_checkbutton(label=gui.player.viewParty()[2].name + " script",
command = lambda: loadScript(gui,gui.player,gui.player.viewParty()[2].name,script3State),variable = script3State,onvalue=1, offvalue=0,
selectcolor=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	scriptSub.add_checkbutton(label=gui.player.viewParty()[3].name + " script",
command = lambda: loadScript(gui,gui.player,gui.player.viewParty()[3].name,script4State),variable = script4State,onvalue=1, offvalue=0,
selectcolor=Defs.fg,background=Defs.bg,activebackground=Defs.bg,activeforeground=Defs.active)
	menu.add_cascade(label="Party Scripts",menu=scriptSub)

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

def loadScript(gui,player,name,state):
	if state.get() == 0:
		pass
	else:
		scriptMenu = tkinter.Toplevel()
		scriptMenu.title = "Load Script"
		scriptMenu.config(width = 300,height = 200,bg=Defs.bg)
		scriptName = tkinter.Entry(scriptMenu,width = 50,bg=Defs.bg,fg=Defs.fg,insertbackground=Defs.fg)
		scriptName.insert(0,"Enter Script Name")
		scriptName.pack()
		loadButton = tkinter.Button(scriptMenu,text="Load",command=lambda: assignScript(gui,player,name,state,scriptName.get(),scriptMenu),bg=Defs.bg,fg=Defs.fg,activebackground=Defs.active)
		loadButton.pack()

def assignScript(gui,player,name,state,script,menu):
	menu.destroy()
	try:
		spec = util.spec_from_file_location("module.name",os.getcwd()+"/Scripts/" + script)
		scriptMod = util.module_from_spec(spec)
		sys.modules["module.name"] = scriptMod
		spec.loader.exec_module(scriptMod)
		playThread(player,name,state,scriptMod).start()
	except:
		gui.updateOutputList("Incorrect Script Name. Include '.py'")

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