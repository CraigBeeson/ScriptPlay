import time

def main(player,charName,active):
	while active.get():
		if player.checkBusy(charName):
			pass
		else:
			player.mine(charName)
		time.sleep(1)