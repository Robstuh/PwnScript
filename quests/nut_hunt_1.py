from com.pwnxile import GameEngine

# Made by Ed and Robbie
# Release date: 9th January 2013

monkeys_uncle_id = 1453
World.addNonCombatNpc(monkeys_uncle_id, 3092, 3492, 0, 0)

def configure_quest_1():
	quest_id = 1 # unique id for quest
	quest_name = 'Nut Hunt I' # name of quest
	quest_stages = 5 # final stage id when quest is completed
	World.addQuest(quest_id, quest_name, quest_stages)

def first_click_npc_1453(player): #monkeys uncle
	quest_stage = player.getQuest(0).getStage()
	if quest_stage == 0:
		player.startChat(500)
		
def pick_bush(player):
	if player.getFunction().checkSpace(1):
		takeNuts(player)
	else:
		player.sendMessage("You do not have enough inventory space to pick monkey nuts.")

def take_nuts(player):
	player.startAnimation(2292)
	player.addItem(4012)
	player.sendMessage("You pick some monkey nuts from the bush.")

def first_click_object_3513(player):
	pick_bush(player)
		
def npc_1453(player, npcId): #monkeys uncle
	player.sendMessage("Doesn't look like the monkey feels like chatting right now.")