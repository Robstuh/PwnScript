v_wep_shop = Shop("Varrock Weapon Store", 53)
v_wep_shop.addItem(ShopItem(4587, 1))

def first_click_npc_551(player):
	player.startChat(10140)

def second_click_npc_551(player):
	player.getShop().openShop(53)
	
def chat_10140(player):
	player.npcChat("Hello there " + str(player.playerName) + ", would you like", "to purchase some fine weapons?")
	player.nextChat(10141)

def chat_10141(player):
	player.playerChat("Perhaps, show me what you have for sale.")
	player.nextChat(10142)

def chat_10142(player):
	player.getShop().openShop(53)


