# NPC Config Script
# Zaff - 546
# Author Robbie

zaffs_superior_staves = Shop("Zaff's Superior Staves", 49)

World.addNonCombatNpc(546, 3203, 3435, 0, 1)

def first_click_npc_546(player): 
	player.npcChat("wat")
	player.endChat()

def second_click_npc_546(player): 
	player.getShop().openShop(49)
