from com.pwnxile.core import World

# Made by Robbie
# Quest seems flawless at present
# Bugs will undoubtedly be discovered

#Release date: 20th December 2012

santa_id = 1552
diango_id = 970
thief_id = 283
thief_key_item = 432
xmas_present = 6542
diango_shop_id = 39

def configure_quest_0():
	quest_id = 0 #unique id for quest
	quest_name = 'A Christmas Crime' #name of quest
	quest_stages = 6 #final stage id when quest is completed
	
	World.addQuest(quest_id, quest_name, quest_stages)
	World.addNonCombatNpc(santa_id, 3079, 3504, 0, 1)
	World.addNonCombatNpc(diango_id, 3080, 3250, 0, 1)
	World.addCombatNpc(thief_id, 3097, 3260, 0, 0, 200, 9, 30, 120)
	World.addObject(2183, 3093, 3240)
	
def click_item_6542(player):
	player.playerChat("I should take the presents back to Santa.")
	
def kill_npc_283(player):
	quest_stage = player.getQuest(0).getStage()
	if quest_stage == 2:
		player.getQuest(0).setStage(3)
		player.addItem(thief_key_item)
		player.playerChat("I wonder what it is this key unlocks...?")
	
def first_click_object_2183(player):
	quest_stage = player.getQuest(0).getStage()
	if quest_stage == 3 and player.hasInventorySpace(3) and player.hasItem(thief_key_item):
		player.boxMessage("You open the chest and find some presents.")
		player.addItem(xmas_present)
		player.addItem(xmas_present)
		player.addItem(xmas_present)
		player.getQuest(0).setStage(4)
	elif quest_stage == 3 and not player.hasInventorySpace(3):
		player.boxMessage("You don't have enough inventory space to open this chest.")
	elif quest_stage == 3 and not player.hasItem(thief_key_item):
		player.boxMessage("You don't have the key.")
	else:	
		player.boxMessage("The chest is empty.")
	
def first_click_npc_1552(player): #talk-to santa
	prayer_level = player.getLevel("prayer")
	quest_stage = player.getQuest(0).getStage()
	if quest_stage == 0 and prayer_level < 31:
		player.boxMessage("You need a prayer level of 31 or higher to start this quest.")
	elif quest_stage == 0 and prayer_level > 30:
		player.dialogueOption("Ask about Christmas", 2000, "Offer assistance", 2006)
	elif quest_stage == 1:
		player.startChat(2012)
	elif quest_stage == 4:
		player.startChat(2035)
	elif quest_stage == 5:
		player.startChat(2039)
	elif quest_stage == 6:
		player.startChat(2047)
	else:
		player.startChat(2014)

def first_click_npc_970(player): #talk-to diango	
	quest_stage = player.getQuest(0).getStage()
	if quest_stage == 1:
		player.startChat(2015)
	elif quest_stage == 3:
		player.startChat(2033)
	else:
		player.startChat(2014)

def second_click_npc_970(player): #trade diango
	quest_stage = player.getQuest(0).getStage()
	if quest_stage == 6:
		player.getShop().openShop(diango_shop_id)
	else:
		player.boxMessage("You must have completed @dre@A Christmas Crime@bla@ to access this shop")
	
def chat_2000(player):
	player.playerChat("Hello Santa, how are the preparations going?")
	player.nextChat(2001)

def chat_2001(player):
	player.npcChat("Not so well unfortunetly " + str(player.playerName) + ".")
	player.nextChat(2002)
	
def chat_2002(player):
	player.playerChat("What's the matter?")
	player.nextChat(2003)
	
def chat_2003(player):
	player.npcChat("Some christmas presents have been stolen!")
	player.nextChat(2004)
	
def chat_2004(player):
	player.playerChat("Oh no that's terrible news!")
	player.nextChat(2005)
	
def chat_2005(player):
	player.npcChat("Yep, Christmas is ruined :(")
	player.endChat()
	
def chat_2006(player):
	player.playerChat("Hey Santa, can I help you out?")
	player.nextChat(2007)
	
def chat_2007(player):
	player.npcChat("Yes you can!", "I need someone to recover some stolen presents.")
	player.nextChat(2008)
	
def chat_2008(player):
	player.playerChat("Where can I find them?")
	player.nextChat(2009)
	
def chat_2009(player):
	player.npcChat("There's a guy in draynor, goes by the name Diango.", "I've been told he knows where they are", "but he won't tell me!")
	player.nextChat(2010)
	
def chat_2010(player):
	player.playerChat("Well I might be able to extract", "some information from him!")
	player.nextChat(2011)
	
def chat_2011(player):
	player.getQuest(0).setStage(1)
	player.refreshQuestTab()
	player.npcChat("I would be very pleased if you could.")
	player.endChat()
	
def chat_2012(player):
	player.playerChat("What is it you want me to do again?")
	player.nextChat(2013)
	
def chat_2013(player):
	player.npcChat("I need you to get information from Diango", "in draynor, I think he knows where the", "stolen presents are located.")
	player.endChat()
	
def chat_2014(player):
	player.npcChat("Can't you see I'm busy?")
	player.endChat()
	
def chat_2015(player):
	player.playerChat("Hi there Diango.")
	player.nextChat(2016)
	
def chat_2016(player):
	player.npcChat("Hey buddy.")
	player.nextChat(2017)
	
def chat_2017(player):
	player.dialogueOption("Wish merry christmas", 2018, "Ask for the presents", 2020, "Ask about draynor", 2024)
	
def chat_2018(player):
	player.playerChat("Merry Christmas!")
	player.nextChat(2019)
	
def chat_2019(player):
	player.npcChat("Merry Christmas to you too!")
	player.nextChat(2017)

def chat_2020(player):
	player.playerChat("Where are the presents!")
	player.nextChat(2021)
	
def chat_2021(player):
	player.npcChat("What presents?")
	player.nextChat(2022)
	
def chat_2022(player):
	player.playerChat("Santa had some christmas presents stolen!", "he said you know where they might be located")
	player.nextChat(2023)
	
def chat_2023(player):
	player.npcChat("Ah sorry, I don't know anything about that I'm afraid!")
	player.nextChat(2017)
	
def chat_2024(player):
	player.playerChat("What's draynor like these days?")
	player.nextChat(2025)
	
def chat_2025(player):
	player.npcChat("It's okay, been very quiet these past months though", "I remember the days when these streets",  "were packed with people and", "now all we get are damn pickpockets!")
	player.nextChat(2026)
	
def chat_2026(player):
	player.playerChat("Pickpockets eh?")
	player.nextChat(2027)
	
def chat_2027(player):
	player.npcChat("Yes indeed.", "Mind you they aren't the worst thieves", "you find around here.")
	player.nextChat(2028)
	
def chat_2028(player):
	player.playerChat("Oh really?")
	player.nextChat(2029)
		
def chat_2029(player):
	player.npcChat("There's a guy living down the road to the east,", "he never used to be able to afford to buy", "from me, however recently he seems", "to have come into a lot of money.")
	player.nextChat(2030)
	
def chat_2030(player):
	player.playerChat("He could be the same thief who stole from santa!")
	player.nextChat(2031)
	
def chat_2031(player):
	player.npcChat("Perhaps...")
	player.nextChat(2032)
	
def chat_2032(player):
	player.getQuest(0).setStage(2)
	player.playerChat("I better go investigate then.")
	player.endChat()
	
def chat_2033(player):
	player.playerChat("I don't think that thief will",  "be bothering you anymore...")
	player.nextChat(2034)
	
def chat_2034(player):
	player.npcChat("Really?", "That's good.")
	player.endChat()
	
def chat_2035(player):
	player.playerChat("I think I've found the presents!")
	player.nextChat(2036)

def chat_2036(player):
	player.npcChat("Excellent, hand them over.")
	player.nextChat(2037)
	
def chat_2037(player):
	if player.hasItem(xmas_present, 3):
		player.dialogueOption("Hand over presents", 2038, "Taunt santa", 2044)
	else:
		player.playerChat("Oops, I don't have them anymore.")
		player.endChat();
	
def chat_2038(player):
	player.boxMessage("You hand over the 3 presents.")
	player.deleteItem(xmas_present, 3)
	player.getQuest(0).setStage(5)
	player.nextChat(2039)
	
def chat_2039(player):
	player.npcChat("*examines*")
	player.nextChat(2040)
	
def chat_2040(player):
	player.npcChat("Yes that's all of them, thank you so much.", "How did you find them?")
	player.nextChat(2041)
	
def chat_2041(player):
	player.playerChat("A thief in draynor had taken them,", "so I killed him.")
	player.nextChat(2042)
	
def chat_2042(player):
	player.npcChat("Good riddance!")
	player.nextChat(2043)
	
def chat_2043(player):
	player.getQuest(0).setStage(6)
	player.refreshQuestTab()
	player.completeQuest("A Christmas Crime", "Access to Diango's shop", "2,500,000 coins", "20 px points", "1 quest point")
	player.nextChat(0)
	player.addCash(2500000)
	player.addPxp(20)
	
def chat_2044(player):
	player.playerChat("I think I might keep them actually.")
	player.nextChat(2045)
	
def chat_2045(player):
	player.npcChat("BUT I NEED THEM!!!", "HAND THEM OVER PLEASEEEEEEEE", "CHRISTMAS WILL BE RUINED OTHERWISE!!!!")
	player.nextChat(2046)
	
def chat_2046(player):
	player.playerChat("Oh alright, keep your hat on.")
	player.nextChat(2038)
	
def chat_2047(player):
	player.npcChat("Thanks for saving Christmas!")
	player.nextChat(2048)
	
def chat_2048(player):
	player.playerChat("No problemo.")
	player.endChat()
	