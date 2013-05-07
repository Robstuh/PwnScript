from com.pwnxile.world.shops import Shop
from com.pwnxile.world.shops import ShopItem

aubury_shop = Shop("Aubury's Rune Shop", 52)
aubury_shop.addItem(ShopItem(554, 300))
aubury_shop.addItem(ShopItem(555, 300))
aubury_shop.addItem(ShopItem(556, 300))
aubury_shop.addItem(ShopItem(557, 300))
aubury_shop.addItem(ShopItem(558, 300))
aubury_shop.addItem(ShopItem(559, 300))
aubury_shop.addItem(ShopItem(560, 300))

aubury_spawn = World.addNonCombatNpc(553, 3253, 3402, 0, 1)

def first_click_npc_553(player):
	player.startChat(10100)

def second_click_npc_553(player):
	player.getShop().openShop(52)

def third_click_npc_553(player):
	aubury_spawn.startAnimation(1818)
	aubury_spawn.gfx0(343)
	aubury_spawn.turnNpc(player.getX(), player.getY())
	aubury_spawn.forceChat("Senventior disthine molenko!")
	player.getTask().teleport(2911, 4832, 0)
	
def chat_10100(player):
	player.npcChat("Do you want to buy some runes?")
	player.nextChat(10101)
	
def chat_10101(player):
    player.dialogueOption("Yes please!", 10102, "Oh, it's a rune shop. No thank you, then.", 10103)
	
def chat_10102(player):
	player.getShop().openShop(52)
	
def chat_10103(player):
	player.playerChat("Oh, it's a rune shop. No thank you, then.")
	player.nextChat(10104)
	
def chat_10104(player):
	player.npcChat("Oh, well if you find someone who does want runes, please", "send them my way.")
	player.closeChat()
	
	