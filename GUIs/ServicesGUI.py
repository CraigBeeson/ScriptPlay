import tkinter

def main(gui,service,serviceType):
	gui.clearDisplay()
	button = tkinter.Button(gui.frame0, text='End Service', width=10, command=lambda: destroyService(gui,service,serviceType),background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg,activeforeground=Defs.active).pack()
	if serviceType == "client":
		clientService(gui,service)
	elif serviceType == "server":
		pass

def clientService(gui,client):
	text = tkinter.StringVar(gui.root)
	tkinter.Entry(gui.frame0,bg=Defs.bg,fg=Defs.fg,textvariable=text).pack()
	tkinter.Button(gui.frame0, text='Send command', width=12, command=lambda: sendCommand(gui,client,text.get()+"\n"),background=Defs.bg,fg=Defs.fg,activebackground=Defs.bg,activeforeground=Defs.active).pack()

def sendCommand(gui,client,command):
	client.send(bytes(command,'utf-8'))
	recv_len = 1
	response = ""
	while recv_len:
		data = (client.recv(4096))
		recv_len = len(data)
		response += data.decode()
		if recv_len < 4096:
			break
	try:
		gui.updateOutputList(response.decode())
	except:
		gui.updateOutputList(response)

def destroyService(gui,service,serviceType):
	i = gui.serviceList.index([service,serviceType])
	gui.services.delete(i)
	if serviceType=="client" or serviceType=="server":
			service.close()
	del gui.serviceList[i]
	gui.updateOutputList(serviceType + " service terminated.")
	gui.clearDisplay()