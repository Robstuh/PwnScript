# NPC Config Script
# Lowe - 550
# Author Robbie

World.addNonCombatNpc(550, 3231, 3424, 0, 1)

def first_click_npc_550(player): 
	player.npcChat("wat")
	player.endChat()

def second_click_npc_550(player): 
	player.getShop().openShop(3)
