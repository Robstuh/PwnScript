from com.pwnxile.world.shops import Shop
from com.pwnxile.world.shops import ShopItem

my_shop = Shop("Fur Stall", 45)
my_shop.addItem(ShopItem(948, 10))
my_shop.addItem(ShopItem(958, 10))

fur_trader = World.addNonCombatNpc(573, 3081, 3251, 0, 1)

def first_click_npc_573(player):
	fur_trader.forceChat("Not right now " + str(player.playerName) + ".")

def second_click_npc_573(player):
	player.getShop().openShop(45)
