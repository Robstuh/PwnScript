# NPC Config Script
# Baraek - 547
# Author Robbie
from com.pwnxile.core import World

baraek = World.addNonCombatNpc(547, 3217, 3433, 0, 1)

def first_click_npc_547(player): 
	baraek.forceChat("I could say something...")
