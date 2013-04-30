pk_gear_shop = Shop("Pking Gear", 48)
pk_gear_shop.addItem(ShopItem(11694, 1))

def first_click_npc_4513(player):
	player.startChat(5503)

def second_click_npc_4513(player):
	player.getShop().openShop(48)
	
def chat_5503(player):
	player.playerChat("Do you have anything for sale?")
	player.nextChat(5504)
	
def chat_5504(player):
	player.npcChat("ye i sell pk gear m8", "best pk gear ever u know", "u wont find pk gear better than mine.", "ok m8")
	player.nextChat(5505)
	
def chat_5505(player):
	player.getShop().openShop(48)
	player.endChat()