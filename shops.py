from com.pwnxile.world.shops import Shop
from com.pwnxile.world.shops import ShopItem

my_shop = Shop("Fur Stall", 45)
my_shop.addItem(ShopItem(948, 10))
my_shop.addItem(ShopItem(958, 10))

World.addNonCombatNpc(573, 3085, 3497, 0, 1)

def second_click_npc_573(player):
	player.getShop().openShop(45)