lunar_clothing_store = Shop("Lunar Clothing Store", 46)
lunar_clothing_store.addItem(ShopItem(9084, 1))
lunar_clothing_store.addItem(ShopItem(9097, 1))
lunar_clothing_store.addItem(ShopItem(9098, 1))
lunar_clothing_store.addItem(ShopItem(9099, 1))
lunar_clothing_store.addItem(ShopItem(9100, 1))
lunar_clothing_store.addItem(ShopItem(9101, 1))
lunar_clothing_store.addItem(ShopItem(9102, 1))

def first_click_npc_4518(player):
	player.startChat(5500)

def second_click_npc_4518(player):
	player.getShop().openShop(46)
	
def chat_5500(player):
	player.playerChat("Do you have anything for sale?")
	player.nextChat(5501)
	
def chat_5501(player):
	player.npcChat("Yes, I sell various lunar clothing.", "Perhaps you are interested in purchasing.")
	player.nextChat(5502)
	
def chat_5502(player):
	player.getShop().openShop(46)
	player.endChat()