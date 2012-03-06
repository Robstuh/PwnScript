from org.pwnxile.core import Script

def pick_bush(player):
	if player.getFunction().checkSpace(1):
		takeNuts(player)
	else:
		player.sendMessage("You do not have enough inventory space to pick monkey nuts.")

def take_nuts(player):
	player.startAnimation(2292)
	player.addItem(4012)
	player.sendMessage("You pick some monkey nuts from the bush.")

def object_3513(player, obId, obX, obY):
	if player.withinInteractionDistance(obX, obY, 0):
		pick_bush(player)