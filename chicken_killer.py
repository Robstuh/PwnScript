from org.pwnxile.core import Script

def npckill_41(killer):
	if killer.chickenKills < 10:
		killer.chickenKills += 1
	else:
		killer.sendMessage("You receive 1 PxP for killing 10 chickens.")
		killer.chickenKills = 0