World.addNonCombatNpc(2625, 2477, 5147, 0, 0)#tzhaar shop

def first_click_npc_2625(player):
	player.startChat(2600)
	
def chat_2600(player):
	player.playerChat("Hello, do you have anything for sale?")
	player.nextChat(2601)
	
def chat_2601(player):
	player.npcChat("Yes indeed.", "I am a crafter obsidian items,", "I will however sell to you in the", "Tzhaar currency Tokkul.")
	player.nextChat(2602)
	
def chat_2602(player):
	player.playerChat("Show me the goods!")
	player.nextChat(2603)

def chat_2603(player):
	player.getShop().openShop(29)
	
def use_item_6571_on_1755(player):
	cut_onyx(player)
	
def use_item_1755_on_6571(player):
	cut_onyx(player)

def use_item_1755_on_6573(player):
	show_onyx_craft_options(player)
	
def use_item_6573_on_1755(player):
	show_onyx_craft_options(player)

def show_onyx_craft_options(player):
	player.dialogueOption("Make Onyx Ring", 2604, "Make Onyx Necklace", 2605, "Make Onyx Amulet", 2606)

def chat_2604(p):
	craft_onyx(p, 6575)

def chat_2605(p):
	craft_onyx(p, 6577)

def chat_2606(p):
	craft_onyx(p, 6581)
	
def craft_onyx(player, new_item):
	player.getFunction().closeAllWindows()
	player.endChat()
	if player.hasItem(6573) and player.getLevel("crafting") > 89:
		player.deleteItem(6573)
		player.addItem(new_item)
		player.startAnimation(888)
		player.getFunction().addSkillXP(500000, 12)
		player.sendMessage("You crafting the gem into a " + str(player.getItems().getItemName(new_item)) + ".") 
	else:
		player.boxMessage("You need a @blu@Crafting@bla@ level of at least @blu@90@bla@ to craft onyx.")

def cut_onyx(player):
	if player.getLevel("crafting") > 89:
		player.deleteItem(6571)
		player.addItem(6573)
		player.sendMessage("You use the chisel to cut the onyx.")
		player.startAnimation(888)
		player.getFunction().addSkillXP(250000, 12)
	else:
		player.boxMessage("You need a @blu@Crafting@bla@ level of at least @blu@90@bla@ to cut onyx.")

def cast_spell_6003_on_6575(player, slot):
	if player.hasItem(557, 20) and player.hasItem(554, 20) and player.hasItem(564, 1):
		enchant_jewelry(player, 6575, 6583)
	else:
		player.sendMessage("You don't have the required runes to cast this spell")

def cast_spell_6003_on_6577(player, slot):
	if player.hasItem(557, 20) and player.hasItem(554, 20) and player.hasItem(564, 1):
		enchant_jewelry(player, 6577, 11128)
	else:
		player.sendMessage("You don't have the required runes to cast this spell")
		
def cast_spell_6003_on_6581(player, slot):
	if player.hasItem(557, 20) and player.hasItem(554, 20) and player.hasItem(564, 1):
		enchant_jewelry(player, 6581, 6585)
	else:
		player.sendMessage("You don't have the required runes to cast this spell")
			
def enchant_jewelry(player, old_item, new_item):
	if player.getLevel("magic") > 86:
		player.deleteItem(old_item)
		player.deleteItem(557, 20)
		player.deleteItem(554, 20)
		player.deleteItem(564, 1)
		player.startAnimation(712)
		player.getFunction().addSkillXP(250000, 6)
		player.getItems().addItem(new_item)
		player.sendMessage("You enchant the " + str(player.getItems().getItemName(old_item)) + " and it becomes a " + str(player.getItems().getItemName(new_item)) + " .")
	else:
		player.sendMessage("You need a Magic level of 87 to cast this spell.")