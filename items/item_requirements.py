points_required = 10
def wear_item_9813(player):
	if player.getQuestPoints() < points_required:
		player.boxMessage("You need at least @dre@" + str(points_required) + " quest points@bla@ to wear this cape.")
	else:
		player.getItems().wearItem(player.wearId, player.wearSlot)

def wear_item_4587(player):
	if player.getQuest(35).getStage() < 15:
		player.boxMessage("You must have completed Monkey Madness to wield a Dragon Scimitar.")
	else:
		player.getItems().wearItem(player.wearId, player.wearSlot)
