lunar_general_store = Shop("General Store", 47)
lunar_general_store.sell = 1

def first_click_npc_4516(player):
	player.startChat(5503)

def second_click_npc_4516(player):
	player.getShop().openShop(47)
	
def chat_5503(player):
	player.playerChat("Do you have anything for sale?")
	player.nextChat(5504)
	
def chat_5504(player):
	player.npcChat("Yes I sell various items and am also", "willing to purchase items from players", "for a good price.")
	player.nextChat(5505)
	
def chat_5505(player):
	player.getShop().openShop(47)
	player.endChat()