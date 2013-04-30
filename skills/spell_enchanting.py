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
