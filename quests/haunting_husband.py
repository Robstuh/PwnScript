#Release date 13th January 2013
#Quest Length = Medium

#NPCs
lesser_demon_id = 82
witch_id = 922
ghost_id = 1697
lady_servil_id = 264

#Objects
chest_id = 2436

#Items
reg_bones_id = 527
portrait_id = 666
power_amulet_id = 1731
chest_key_id = 4273

#Quest configuration
def configure_quest_4():
    quest_id = 4
    quest_name = 'The Haunting Husband'
    quest_stages = 10
    World.addQuest(quest_id, quest_name, quest_stages)
    World.addNonCombatNpc(lady_servil_id, 2757, 3496, 0, 1)
    World.addNonCombatNpc(witch_id, 3478, 3476, 0, 1)
    World.addNonCombatNpc(ghost_id, 3251, 3193, 0, 1)
    World.addObject(chest_id, 2737, 3573)

#Quest button
def quest_button_4(player):
    quest_stage = player.getQuest(4).getStage()
    if quest_stage == 0:
        player.boxMessage("I can start this quest by talking to @dre@Lady Servil@bla@ at Camelot castle.")
    elif quest_stage == 1:
        player.boxMessage("I should go find Sir Phil's coffin at the Lumbridge graveyard")
    elif quest_stage == 2:
        player.boxMessage("I better talk to Lady Servil again...")
    elif quest_stage == 3:
        player.boxMessage("The witch in Canifis will know how to speak to a ghost.")
    elif quest_stage == 4:
        player.boxMessage("Bring an amulet of power and 50 noted bones to the witch.")
    elif quest_stage == 5:
        player.boxMessage("I should probably go speak with the ghost now.")
    elif quest_stage == 6:
        player.boxMessage("I must slay @dre@Lesser Demons@bla@ until I get a key.")
    elif quest_stage == 7:
        player.boxMessage("I should bring the key to the ghost Sir Phil.")
    elif quest_stage == 8:
        player.boxMessage("Sir Phil said the chest would be at a house on the western site of the castle.")
    elif quest_stage == 9:
        player.boxMessage("Talk to @dre@Lady Servil@bla@ to recieve your reward.")
    elif quest_stage == 10:
        player.boxMessage("I have completed @dre@The Haunting Husband@bla@.")

#Portrait
def click_item_666(player):
    player.playerChat("This looks exactly like Lady Servil")

#Chest-key	
def click_item_4273(player):
    player.playerChat("I should probably take this to the ghost Sir Phil.")

#Lady Servil	
def first_click_npc_264(player):
    quest_stage = player.getQuest(4).getStage()
    if quest_stage == 0:
        player.dialogueOption("Ask what's wrong", 7000, "Say goodbye", 7008)
    elif quest_stage == 2:
        player.startChat(7014)
    elif quest_stage == 9:
        player.startChat(7052)
    elif quest_stage == 10:
        player.npcChat("Hello " + str(player.playerName) + ", thank you for helping my husband and I.")
    else:
        player.playerChat("I better not disturb Lady Servil...")

#Ghost		
def first_click_npc_1697(player):
    quest_stage = player.getQuest(4).getStage()
    if quest_stage == 1:
        player.startChat(7010)
    elif quest_stage == 5:
        player.startChat(7037)
    elif quest_stage == 7 and player.hasItem(chest_key_id):
        player.dialogueOption("Never mind", 7044, "I got the key", 7045)
    elif quest_stage == 7 and not player.hasItem(chest_key_id):
        player.playerChat("Ooops, I forgot the key...")
    elif quest_stage == 9 and player.hasItem(portrait_id):
        player.startChat(7050)
    elif quest_stage == 9 and not player.hasItem(portrait_id):
        player.playerChat("I better bring the portrait first...")
    else:
        player.playerChat("Maybe I should just leave Sir Phil alone")

#Witch		
def first_click_npc_922(player):
    quest_stage = player.getQuest(4).getStage()
    if quest_stage == 3:
        player.startChat(7018)
    elif quest_stage == 4 and player.hasItem(reg_bones_id, 50) and player.hasItem(power_amulet_id):
        player.startChat(7029)
    elif quest_stage == 4 and not player.hasItem(reg_bones_id, 50) and player.hasItem(power_amulet_id):
        player.npcChat("Don't come back again unless you have the materials!")
    else:
        player.playerChat("I probably shouldn't disturb the witch right now.")

#Lesser Demon slaying
def kill_npc_82(player):
    if player.hasAttribute("lesser_kills"):
        handle_lesser_kill(player)
    else:
        player.addAttribute("lesser_kills", 1)
        
def handle_lesser_kill(player):
    quest_stage = player.getQuest(4).getStage()
    if quest_stage == 6 and player.getAttribute("lesser_kills") > 24:
    	player.addAttribute("lesser_kills", 0)
        player.sendMessage("You have received a key.")
        player.addItem(chest_key_id)
    	player.getQuest(4).setStage(7)
        player.refreshQuestTab()
    else:
        player.addAttribute("lesser_kills", player.getAttribute("lesser_kills") + 1)

#The chest
def first_click_object_2436(player):
    quest_stage = player.getQuest(4).getStage()
    if quest_stage == 8 and player.hasItem(chest_key_id) and player.hasInventorySpace(1) and not player.hasItem(portrait_id):
        player.boxMessage("You open the chest and find a portrait of Lady Servil.")
        player.addItem(portrait_id)
        player.getQuest(4).setStage(9)
    elif quest_stage == 8 and not player.hasInventorySpace(1):
        player.boxMessage("You don't have enough inventory space to open this chest.")
    elif quest_stage == 8 and not player.hasItem(chest_key_id):
        player.boxMessage("You must bring the key, to open the chest.")
    else:	
        player.boxMessage("Nothing interesting here.")

#Chat dialogues	
def chat_7000(player):
    player.playerChat("Hello milady, why are you so sad?")
    player.nextChat(7001)
    
def chat_7001(player):
    player.npcChat("My husband Sir Phil was murdered", "and now he's haunting the castle")
    player.nextChat(7002)
    
def chat_7002(player):
    player.dialogueOption("Ask if you can help", 7003, "Say goodbye", 7008)

def chat_7003(player):
    player.playerChat("Is there anything I can do to help?")
    player.nextChat(7004)
    
def chat_7004(player):
    player.npcChat("There actually is, if you're up for an adventure.", "My husband's coffin is located at the Lumbridge graveyard.", "Maybe you could ask him to stop haunting the castle?")
    player.nextChat(7005)
    
def chat_7005(player):
    player.dialogueOption("Accept the Quest", 7006, "Decline the Quest", 7009)
    
def chat_7006(player):
    player.getQuest(4).setStage(1)
    player.refreshQuestTab()
    player.playerChat("I'll do my best to make your husband", "stop haunting the castle.")
    player.nextChat(7007)

def chat_7007(player):
    player.npcChat("Thank you!")
    player.endChat()

def chat_7008(player):
    player.playerChat("I'm sorry to disturb you, goodbye!")
    player.endChat()
    
def chat_7009(player):
    player.playerChat("Naah, it sounds too boring, I'll go slay some goblins instead.")
    player.endChat()
    
def chat_7010(player):
    player.npcChat("Wwwhhooooooo!!")
    player.nextChat(7011)

def chat_7011(player):
    player.playerChat("Excuse me, but could you please repeat that?")
    player.nextChat(7012)
    
def chat_7012(player):
    player.npcChat("Wwwhhooooooo!!")
    player.nextChat(7013)
    
def chat_7013(player):
    player.getQuest(4).setStage(2)
    player.refreshQuestTab()
    player.playerChat("I should probably go speak to Lady Servil again...")
    player.endChat()

def chat_7014(player):
    player.npcChat("Hello " + str(player.playerName) + ", did you talk to my husband?")
    player.nextChat(7015)
    
def chat_7015(player):
    player.playerChat("I tried, but all he said was @dre@Wwwhhoooooo!!")
    player.nextChat(7016)
    
def chat_7016(player):
    player.getQuest(4).setStage(3)
    player.refreshQuestTab()
    player.npcChat("I know a witch in Canifis, she'll maybe know what to do.", "Please go to Canifis, just tell the witch I sent you.")
    player.nextChat(7017)

def chat_7017(player):
    player.playerChat("Alright...")
    player.endChat()
    
def chat_7018(player):
    player.npcChat("What do you want from me!")
    player.nextChat(7019)
    
def chat_7019(player):
    player.dialogueOption("Wh... Wh... Who are you?", 7020, "Lady Servil sent me.", 7022)

def chat_7020(player):
    player.playerChat("Wh... Wh... Who are you?")
    player.nextChat(7021)
    
def chat_7021(player):
    player.npcChat("I am the great witch of Canifis!", "Now answer my question, what do you want!")
    player.nextChat(7022)
    
def chat_7022(player):
    player.playerChat("I was sent here by Lady Servil.", "Sir Phil got murdered, and I want to speak with him.")
    player.nextChat(7023)
    
def chat_7023(player):
    player.npcChat("So you want to speak to a dead man huh?")
    player.nextChat(7024)
    
def chat_7024(player):
    player.playerChat("Yes, but I don't understand what he's trying to tell me...")
    player.nextChat(7025)
    
def chat_7025(player):
    player.npcChat("You must wield a Ghostspeak amulet,", "to speak with the dead", "If you bring me the materials,", "I will make you the Ghostspeak amulet")
    player.nextChat(7026)

def chat_7026(player):
    player.playerChat("What are the required materials?")
    player.nextChat(7027)
    
def chat_7027(player):
    player.getQuest(4).setStage(4)
    player.refreshQuestTab()
    player.npcChat("Bring me an amulet of power and 50 noted bones.")
    player.nextChat(7028)
    
def chat_7028(player):
    player.playerChat("Alright, see you later")
    player.endChat()

def chat_7029(player):
    player.npcChat("Do you have the materials yet?")
    player.nextChat(7030)
    
def chat_7030(player):
    player.dialogueOption("Yes.", 7031, "No.", 7035)
    
def chat_7031(player):
    player.playerChat("Yes, I brought them with me.")
    player.nextChat(7032)
    
def chat_7032(player):
	player.npcChat("Very good, now give them to me")
	player.nextChat(7033)
    
def chat_7033(player):
	player.deleteItem(reg_bones_id, 50)
	player.deleteItem(power_amulet_id)
	player.getQuest(4).setStage(5)
	player.boxMessage("The witch gives you the power of @dre@Ghostspeak@bla@.")
	player.nextChat(7034)
    
def chat_7034(player):
    player.playerChat("Thank you witch, bye!")
    player.endChat()
    
def chat_7035(player):
    player.npcChat("Are you sure?")
    player.nextChat(7036)
    
def chat_7036(player):
    player.playerChat("No... I might have the items anyways")
    player.nextChat(7032)
    
def chat_7037(player):
    player.playerChat("Hello Sir Phil, do you understand me?")
    player.nextChat(7038)
    
def chat_7038(player):
    player.npcChat("Yes I do, " + str(player.playerName) + ".")
    player.nextChat(7039)
    
def chat_7039(player):
    player.playerChat("Wow, I can't believe this is actually working!", "So... Sir Phil, why are you haunting the Camelot castle?")
    player.nextChat(7040)
    
def chat_7040(player):
    player.npcChat("My murderer took something of mine.", "It's a portrait of my beloved wife Servil.", "I will only find peace if I get the portrait back")
    player.nextChat(7041)
    
def chat_7041(player):
    player.playerChat("Tell me what to do and I'll help!")
    player.nextChat(7042)
    
def chat_7042(player):
	player.getQuest(4).setStage(6)
	player.npcChat("You will find the portrait in a locked chest.", "The key is guarded by Lesser Demons.", "Go out and slay Lesser Demons 'till you get the key.")
	player.nextChat(7043)
	
def chat_7043(player):
    player.playerChat("Okay, I will get you that key!")
    player.endChat()
    
def chat_7044(player):
    player.playerChat("Never mind...")
    player.endChat()
    
def chat_7045(player):
    player.playerChat("After days of fighting, I finally got the key you asked for!")
    player.nextChat(7046)
    
def chat_7046(player):
    player.npcChat("Good job " + str(player.playerName) + ".")
    player.nextChat(7047)
    
def chat_7047(player):
    player.playerChat("What shall I do with the key?")
    player.nextChat(7048)
    
def chat_7048(player):
    player.getQuest(4).setStage(8)
    player.refreshQuestTab()
    player.npcChat("Nearby the castle at the western site there is a house.", "Walk through the gates and continue 'till you see a chest.", "Inside the chest you will fin what I'm searching")
    player.nextChat(7049)
    
def chat_7049(player):
    player.playerChat("Alright, I will find your portrait!")
    player.endChat()
    
def chat_7050(player):
    player.playerChat("I have found the portrait!")
    player.nextChat(7051)
    
def chat_7051(player):
    player.getQuest(4).setStage(9)
    player.refreshQuestTab()
    player.npcChat("Thank you " + str(player.playerName) + ", now I can finally rest.", "You should go tell the good news to my wife")
    player.endChat()
    
def chat_7052(player):
    player.playerChat("Hello Lady Servil, I have some good news.")
    player.nextChat(7053)
    
def chat_7053(player):
    player.npcChat("Please tell me you have talked to my husband.")
    player.nextChat(7054)
    
def chat_7054(player):
    player.playerChat("All he wanted was a portrait of you.", "You husband has finally found peace")
    player.nextChat(7055)
    
def chat_7055(player):
    player.npcChat("I don't even know how to thank you " + str(player.playerName) + "!", "Please accept my humble reward for your great effort.")
    player.nextChat(7056)
    
def chat_7056(player):
    player.endChat()
    player.getQuest(4).setStage(10)
    player.refreshQuestTab()
    player.addCash(25000000)
    player.addPxp(50)
    player.addItem(5033)
    player.addItem(5035)
    player.completeQuest("The Haunting Husband", "25,000,000 coins", "50 px points", "1 quest point", "Zamorak robes")