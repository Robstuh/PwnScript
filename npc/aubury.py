aubury_shop = Shop("Aubury's Rune Shop", 52)
aubury_shop.addItem(ShopItem(560, 100))
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

