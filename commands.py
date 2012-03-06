from org.pwnxile.core import Script
from org.pwnxile.rs2 import PlayerHandler
from org.pwnxile.rs2.content import Staff

def command_staff(player):
	player.sendMessage("There are " + str(Staff.getStaffCount()) + " staff online.")
	player.sendMessage("They are:")
	player.sendMessage(str(Staff.getStaffNames()))
	player.sendMessage("Send one a message for help!")
	
def command_players(player):
	player.sendMessage("There are currently " + str(PlayerHandler.getPlayerCount()) + " players online.")
	
def command_printstaff(player):
	for value in Staff.getStaffList():
		player.sendMessage(value.playerName)