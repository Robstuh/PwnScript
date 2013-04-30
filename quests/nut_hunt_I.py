# Made by Ed and Robbie
# Release date: 9th January 2013

monkeys_uncle_id = 1453
noted_monkey_nuts = 4013
dark_hole = 5947

def configure_quest_1():
	quest_id = 1 # unique id for quest
	quest_name = 'Nut Hunt I' # name of quest
	quest_stages = 2 # final stage id when quest is completed
	World.addQuest(quest_id, quest_name, quest_stages)
	# World.addNonCombatNpc(monkeys_uncle_id, 3084, 3501, 0, 0)
	World.addObject(dark_hole, 3090, 3498)
	
def first_click_object_5947(player):
	quest_stage = player.getQuest(1).getStage()
	if quest_stage == 0:
		player.boxMessage("Speak with the monkeys uncle before going down there.")
	else:
		player.move(Position.NUT_ROOM)
	
def quest_button_1(player):
	quest_stage = player.getQuest(1).getStage()
	if quest_stage == 0:
		player.boxMessage("I can start the Hunt by talking to the monkeys uncle.")
	elif quest_stage == 1:
		player.boxMessage("I need to bring 1000 noted nuts to the monkeys uncle.")
	elif quest_stage == 2:
		player.boxMessage("I have completed the @dre@Nut Hunt@bla@ quest.")
		
def first_click_npc_1453(player):
	quest_stage = player.getQuest(1).getStage()
	if quest_stage == 0:
		player.startChat(500)
	elif quest_stage == 1 and player.hasItem(noted_monkey_nuts, 1000):
		player.startChat(517)
	elif quest_stage == 1:
		player.npcChat("Hurry up and get those nuts!")
	else:
		player.playerChat("He looks pretty grumpy,", "I better not disturb him.")

def first_click_object_12615(player):
	if player.hasInventorySpace(1):
		player.getFunction().pickMonkeyNuts()
	else:
		player.boxMessage("You do not have enough inventory space to pick monkey nuts.")
	
def click_item_4012(player):
	player.playerChat("I don't think I should eat those...")
	
def chat_500(player):
	player.npcChat("Hello, do you have any monkey nuts?")
	player.nextChat(501)

def chat_501(player):
	player.playerChat("Uhhh maybe...")
	player.nextChat(502)

def chat_502(player):
	player.playerChat("...Why?")
	player.nextChat(503)
	
def chat_503(player):
	player.npcChat("I need to get some for my nephews birthday.")
	player.nextChat(504)
	
def chat_504(player):
	player.playerChat("Ah I see.")
	player.nextChat(590)
	
def chat_590(player):
	player.playerChat("How many do you need?")
	player.nextChat(506)
	
def chat_506(player):
	player.npcChat("Ooh I don't know.. how about...")
	player.nextChat(507)
	
def chat_507(player):
	player.npcChat("OVER NINE THOUSAND!")
	player.nextChat(508)
	
def chat_508(player):
	player.playerChat("You have got to be kidding me...")
	player.nextChat(509)
	
def chat_509(player):
	player.npcChat("Hahaha alright, how about 1000?")
	player.nextChat(510)
	
def chat_510(player):
	player.playerChat("Whats in it for me?")
	player.nextChat(511)
	
def chat_511(player):
	player.npcChat("I'll happily pay you 1000 golden coins!")
	player.nextChat(512)
	
def chat_512(player):
	player.playerChat("Uhh no thanks!")
	player.nextChat(513)
	
def chat_513(player):
	player.npcChat("2000?")
	player.nextChat(514)
	
def chat_514(player):
	player.playerChat("...")
	player.nextChat(515)
	
def chat_515(player):
	player.npcChat("10 million?")
	player.nextChat(516)
	
def chat_516(player):
	player.playerChat("Alright then.")
	player.getQuest(1).setStage(1)
	player.refreshQuestTab()
	player.endChat()
	
def chat_517(player):
	player.playerChat("I HAVE YOUR NUTS!")
	player.nextChat(518)
	
def chat_518(player):
	player.npcChat("Excuse me?")
	player.nextChat(519)
	
def chat_519(player):
	player.playerChat("The monkey nuts.")
	player.nextChat(520)
	
def chat_520(player):
	player.npcChat("Oh...thanks.")
	player.nextChat(521)
	
def chat_521(player):
	player.endChat()
	player.getQuest(1).setStage(2)
	player.refreshQuestTab()
	player.addCash(10000000)
	player.completeQuest("Nut Hunt I", "Access to Ape Atol", "10,000,000 coins", "1 Quest Point", "")
