import Defs

class Enemy():
	def __init__(self,name):
		self.name = name
		self.stats = Defs.enemies[name]["stats"]
		self.hp = self.stats["hp"]
	
	def recvDmg(dmg):
		self.hp -= dmg
		if self.hp <= 0:
			self.death()
	
	def death():
		pass