mages_store = Shop("Mages Store", 51)
mages_store.addItem(ShopItem(560, 100))
mage_of_zamorak = 2259
mage_of_zamorak_spawn = World.addNonCombatNpc(mage_of_zamorak, 3260, 3385, 0, 1)

def first_click_npc_2259(player):
	player.startChat(10200)

def second_click_npc_2259(player):
	player.getShop().openShop(51)

def third_click_npc_2259(player):
	mage_of_zamorak_spawn.startAnimation(1818)
	mage_of_zamorak_spawn.gfx0(343)
	mage_of_zamorak_spawn.turnNpc(player.getX(), player.getY())
	mage_of_zamorak_spawn.forceChat("Veniens! Sallakar! Rinnesset!")
	player.getTask().teleport(3039, 4834, 0)

