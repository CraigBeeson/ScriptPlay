import tkinter
import ctypes
import Defs
import GUIs
from Classes import Player
import copy
import time

user32 = ctypes.windll.user32
#the main program gui
class ScriptPlayGUI:
	def __init__(self):
		#create root tkinter frame and set some basic properties
		self.root = tkinter.Tk()
		self.root.minsize(500,500)
		self.root.maxsize(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
		self.root.title("Holy Grail")
		#combat var
		self.__combat = False
		#creates player class
		self.player = Player.Player(self)
		#sets some submenu names
		self.invMenu = None
		self.services = None
		self.partyMenu = None
		#list for background services
		self.serviceList = []
		#upper and lower window frames
		#lower for textoutput from the game
		self.frame0 = None
		self.frame1 = None
		self.outputList = None
		self.root.config(bg=Defs.bg)
		#calls functions to set up the gui
		self.setMenu()
		self.setFrames()
		#temp code to test scripting
		#self.player.mine("Craig")
		#self.player.fish("Dustin")
		#self.player.forage("Jimmy")
		#self.player.hunt("Jonny")
		#self.player.mine("Craig")
		
	#this sets up the menu
	def setMenu(self):
		#test code
		#root menu element
		menu = tkinter.Menu(self.root,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		self.root.config(menu=menu)
		#toolmenu added to root menu, nothing for tools yet
		toolmenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		menu.add_cascade(label='Tools', menu=toolmenu)
		#adds the inventory menu
		self.invMenu = GUIs.InventoryGUI.InvMenu(self,tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg))
		menu.add_cascade(label='Inventory', menu=self.invMenu.menu)
		self.invMenu.setInvMenu()
		#adds the party menu
		self.partyMenu = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		menu.add_cascade(label="Party",menu=self.partyMenu)
		GUIs.PartyGUI.setPMenu(self,self.partyMenu)
		#background services menu
		self.services = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
		menu.add_cascade(label="Services",menu=self.services)

	def setFrames(self):
		#upper frame
		self.frame0 = tkinter.Frame(self.root,bg=Defs.bg,width="500",height="376",name="display",bd=0,highlightbackground=Defs.fg,highlightthickness=2)
		self.frame0.pack(side="top",fill="both",expand=True)
		#lowerframe
		self.frame1 = tkinter.Frame(self.root,bg=Defs.bg,width="500",height="125",name="output",bd=0,highlightbackground=Defs.fg,highlightthickness=2)
		self.frame1.pack(side="bottom",fill="both",expand=True)
		#scroll bars for the bottom or "output" frame
		scrollbar = tkinter.Scrollbar(self.frame1,orient="vertical")
		scrollbar.pack( side = "right", fill = "y")
		scrollbar1 = tkinter.Scrollbar(self.frame1,orient="horizontal")
		scrollbar1.pack(side = "bottom", fill = "x" )
		#output displayed in the bottom frame goes inside this listbox
		self.outputList = tkinter.Listbox(self.frame1,xscrollcommand=scrollbar1.set, yscrollcommand = scrollbar.set,bg=Defs.bg,fg=Defs.fg,name="output" )
		self.outputList.pack( side = "left", fill = "both",expand=True )
		#configure scroll bars
		scrollbar.config( command = self.outputList.yview )
		scrollbar1.config(command=self.outputList.xview)

	#this clears the display
	def clearDisplay(self):
		for item in self.frame0.winfo_children():
			item.destroy()

	#adds lines to the output list and removes excess lines
	def updateOutputList(self,line):
		temp = self.outputList.winfo_children()
		if len(temp)==250:
			temp[0].destroy()
		self.outputList.insert("end",line)

	#function for updating the background services list
	def addService(self,service,serviceType):
		self.serviceList.append([service,serviceType])
		self.services.add_command(label=serviceType,command=lambda: GUIs.ServicesGUI.main(self,service,serviceType))
	
	def viewCombat(self):
		return copy.copy(self.__combat)