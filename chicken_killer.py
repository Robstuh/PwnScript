from org.pwnxile.core import Script

def npckill_41(killer):
	if killer.chickenKills < 10:
		killer.chickenKills += 1
	else:
		killer.sendMessage("You receive 1 PxP for killing 10 chickens.")
		killer.chickenKills = 0
		
def takeNuts(player):
	player.startAnimation(2292)
	player.addItem(4012)
	player.sendMessage("You pick some monkey nuts from the bush.")