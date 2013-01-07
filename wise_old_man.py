# NPC Config Script
# Wise Old Man - 2566
# Author Robbie

def first_click_npc_2566(player): 
	player.startChat(2050)

def chat_2050(player):	
	player.dialogueOption("View cape shop", 2051, "Reset combat levels to 1", 2053)

def chat_2051(player):	
	player.getShop().openSkillcapeShop();
		
def chat_2052(player):
	player.dialogueOption("Confirm level reset", 2053, "Do not reset levels", 0)
	
def chat_2053(player):
	player.getFunction().closeAllWindows()
	if not player.isWieldingItems():
		player.sendMessage("You have reset your combat levels to 1.")
		player.getFunction().resetCombatLevels()
	else:
		player.boxMessage("You must not be wielding any items to do this.")	