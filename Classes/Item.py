import Defs

class Item():
	def __init__(self,name,count=1):
		self.name = name
		self.info = self.getInfo(name)
		self.amount = count
	def getInfo(self,name):
		for i in Defs.items.keys():
			for j in Defs.items[i].keys():
				if name in Defs.items[i][j]:
					return Defs.items[i][j][name]