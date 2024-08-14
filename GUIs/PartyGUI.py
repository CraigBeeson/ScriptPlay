import tkinter
import Defs

def setPMenu(gui,menu):
	partySub = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
	actions(gui,gui.player.viewParty()[0],partySub)
	menu.add_cascade(label=gui.player.viewParty()[0].name,menu=partySub)
	partySub.add_command(label="Equipment",command=lambda: equipment(gui,gui.player.viewParty()[0]))
	partySub.add_command(label="Stats",command=lambda: stats(gui,gui.player.viewParty()[0]))
	partySub1 = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
	actions(gui,gui.player.viewParty()[1],partySub1)
	menu.add_cascade(label=gui.player.viewParty()[1].name,menu=partySub1)
	partySub1.add_command(label="Equipment",command=lambda: equipment(gui,gui.player.viewParty()[1]))
	partySub1.add_command(label="Stats",command=lambda: stats(gui,gui.player.viewParty()[1]))
	partySub2 = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
	actions(gui,gui.player.viewParty()[2],partySub2)
	menu.add_cascade(label=gui.player.viewParty()[2].name,menu=partySub2)
	partySub2.add_command(label="Equipment",command=lambda: equipment(gui,gui.player.viewParty()[2]))
	partySub2.add_command(label="Stats",command=lambda: stats(gui,gui.player.viewParty()[2]))
	partySub3 = tkinter.Menu(menu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
	actions(gui,gui.player.viewParty()[3],partySub3)
	menu.add_cascade(label=gui.player.viewParty()[3].name,menu=partySub3)
	partySub3.add_command(label="Equipment",command=lambda: equipment(gui,gui.player.viewParty()[3]))
	partySub3.add_command(label="Stats",command=lambda: stats(gui,gui.player.viewParty()[3]))

def equipment(gui,character):
	gui.updateOutputList(character.name + " currently has equipped: ")
	for i in character.viewEquipment().keys():
		gui.updateOutputList("          " + i + ": " + character.viewEquipment()[i])

def stats(gui,character):
	gui.updateOutputList(character.name + " current stats: ")
	for i in character.viewStats().keys():
		gui.updateOutputList("          " + i + ": " + str(character.viewStats()[i]))

def actions(gui,character,submenu):
	action = tkinter.Menu(submenu,tearoff=False,background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg)
	submenu.add_cascade(label="Actions",menu = action)
	action.add_command(label="Mine",command=lambda: gui.player.mine(character.name))
	action.add_command(label="Fish",command=lambda: gui.player.fish(character.name))
	action.add_command(label="Forage",command=lambda: gui.player.forage(character.name))
	action.add_command(label="Hunt",command=lambda: gui.player.hunt(character.name))