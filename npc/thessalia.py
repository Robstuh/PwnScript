# NPC Config Script
# Thessalia - 548
# Author Robbie

thessalias_fine_clothes = Shop("Thessalia's Fine Clothes", 50)

World.addNonCombatNpc(548, 3206, 3417, 0, 1)

def first_click_npc_548(player): 
	player.npcChat("wat")
	player.endChat()

def second_click_npc_548(player): 
	player.getShop().openShop(50)

def third_click_npc_548(player):
	player.getFunction().showInterface(3559)
