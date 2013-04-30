from com.pwnxile.core import World

World.addNonCombatNpc(2625, 2477, 5147, 0, 0)#tzhaar shop

def first_click_npc_2625(player):
	player.startChat(2600)
	
def chat_2600(player):
	player.playerChat("Hello, do you have anything for sale?")
	player.nextChat(2601)
	
def chat_2601(player):
	player.npcChat("Yes indeed.", "I am a crafter obsidian items,", "I will however sell to you in the", "Tzhaar currency Tokkul.")
	player.nextChat(2602)
	
def chat_2602(player):
	player.playerChat("Show me the goods!")
	player.nextChat(2603)

def chat_2603(player):
	player.getShop().openShop(29)
