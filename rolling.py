from org.pwnxile.core import Script
from org.pwnxile.rs2 import PlayerHandler

def command_killall(p):
	if(p.playerRights > 2):
		killall()
	
def killall():	
	for players in PlayerHandler.players:
		if(players != None):
			players.deathHandler.deathSequence()			