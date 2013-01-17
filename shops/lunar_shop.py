mc_general_store = Shop("Moon Clan General Store", 46)
mc_general_store.addItem(ShopItem(9084, 1))

melana_moonlander = World.addNonCombatNpc(4516, 2086, 3914, 0, 1)

def second_click_npc_4516(player):
	player.getShop().openShop(46)