from com.pwnxile.core import World
from com.pwnxile.rs2 import Position
from com.pwnxile.rs2 import Location

donor_island = Location.DONOR_ISLAND

def first_click_object_2156(player): # Click the donor portal
	if player.isDonator():
		player.teleport(Position.DONOR_ISLAND_SPAWN)
	else:
		player.boxMessage("You must be a donator to use this portal.")
		
def is_on_island(player): # Check player is on the island
	if donor_island.isInLocation(player):
		return True
	return False
		