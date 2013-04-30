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
