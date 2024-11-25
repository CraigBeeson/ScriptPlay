import time

def main(player,charName,active):
	while active.is_set():
		if player.checkBusy(charName):
			pass
		else:
			player.fish(charName)
		time.sleep(1)