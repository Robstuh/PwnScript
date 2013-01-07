#Release date: TBC
from com.pwnxile.core import World

monkeys_uncle_id = 1453

def configured_quest_1():
	quest_id = 1 # unique id for quest
	quest_name = 'Nut Hunt I' # name of quest
	quest_stages = 5 # final stage id when quest is completed
	World.addQuest(quest_id, quest_name, quest_stages)
	World.addNonCombatNpc(monkeys_uncle_id, 2732, 2783, 0, 1)

def configured_quest_2():
	quest_id = 2 # unique id for quest
	quest_name = 'Nut Hunt II' # name of quest
	quest_stages = 4 # final stage id when quest is completed
	World.addQuest(quest_id, quest_name, quest_stages)
	
def first_click_npc_1453(player): #monkeys uncle
	quest_stage = player.getQuest(0).getStage()
	

def pick_bush(player):
	if player.getFunction().checkSpace(1):
		takeNuts(player)
	else:
		player.sendMessage("You do not have enough inventory space to pick monkey nuts.")

def take_nuts(player):
	player.startAnimation(2292)
	player.addItem(4012)
	player.sendMessage("You pick some monkey nuts from the bush.")

def object_3513(player, obId, obX, obY):
	if player.withinInteractionDistance(obX, obY, 0):
		pick_bush(player)
		
def npc_1453(player, npcId): #monkeys uncle
	player.sendMessage("Doesn't look like the monkey feels like chatting right now.")