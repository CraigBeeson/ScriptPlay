import time

def main(characterList):
	while True:
		for i in characterList:
			if i.busy:
				i.cooldown -= 1
				if i.cooldown <= 0:
					i.busy = False
		time.sleep(1)