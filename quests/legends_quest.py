
#This Quest was created by H E L L 0 aka Wise Old Man
#Release date 11th January 2013
#Quest Length = Long

#NPCs
demon_id = 934
king_roald_id = 648

#Items
rune_bar_id = 2364
addy_bar_id = 2362
steel_bar_id = 2354
cooked_manta_id = 392
silverlight_id = 2402
legends_cape_id = 1052
burnt_bones_id = 528

def configure_quest_3():
    quest_id = 3
    quest_name = 'Legends Quest'
    quest_stages = 5
    World.addQuest(quest_id, quest_name, quest_stages)
    World.addNonCombatNpc(king_roald_id, 3213, 3463, 0, 1)
    World.addCombatNpc(demon_id, 2947, 2898, 0, 1, 250, 35, 120, 120)
    #World.addCombatNpc(demon_id, 2956, 2910, 0, 1) #If more than one demon is to be added in the jungle
    #World.addCombatNpc(demon_id, 2964, 2922, 0, 1) #If more than one demon is to be added in the jungle
    
def quest_button_3(player):
    quest_stage = player.getQuest(3).getStage()
    if quest_stage == 0: 
        player.boxMessage("I can start this quest by speaking to @dre@King Roald@bla@.")
    elif quest_stage == 1:
        player.boxMessage("I must bring the items to King Roald") 
    elif quest_stage == 2:
        player.boxMessage("I must bring 500 cooked manta rays to King Roald") 
    elif quest_stage == 3:
        player.boxMessage("When I'm ready to fight the demon, I have to talk to King Roald") 
    elif quest_stage == 4:
        player.boxMessage("I should bring the burnt bones to King Roald") 
    elif quest_stage == 5:
        player.boxMessage("I have completed the @dre@Legend's Quest@bla@.")
        
def kill_npc_934(player):
    quest_stage = player.getQuest(3).getStage()
    if quest_stage == 3:
        player.getQuest(3).setStage(4)
        player.addItem(burnt_bones_id)
        player.sendMessage("I better bring the bones to King Roald.")
        player.getFunction().startTeleport2(3094, 3470, 0)

def click_item_528(player):
    player.playerChat("I better bring the bones to King Roald")	

def first_click_npc_648(player):
    smithing_level = player.getLevel("smithing")
    fishing_level = player.getLevel("fishing")
    quest_stage = player.getQuest(3).getStage()
    if quest_stage == 0 and fishing_level < 90:
        player.boxMessage("You need a fishing level of 90 or higher to start this quest.")
    elif quest_stage == 0 and smithing_level < 85:
        player.boxMessage("You need a smithing level of 85 or higher to start this quest.")  
    elif quest_stage == 0 and fishing_level > 89 and smithing_level > 84:
        player.startChat(5008)
    elif quest_stage == 1 and player.hasItem(rune_bar_id, 10) and player.hasItem(addy_bar_id, 20) and player.hasItem(steel_bar_id, 100):
        player.startChat(5017)
    elif quest_stage == 1:
        player.npcChat("Why are you back already?", "Hurry up and get me the items!")
    elif quest_stage == 2 and player.hasItem(cooked_manta_id, 500):
        player.startChat(5021)
    elif quest_stage == 2:
        player.npcChat("The dwarfs are hungry, please hurry up!")
    elif quest_stage == 3 and player.hasItem(silverlight_id):
        player.startChat(5035)
    elif quest_stage == 3:
        player.npcChat("You must bring the Silverlight, to slay the demon!")
    elif quest_stage == 4 and player.hasItem(burnt_bones_id):
        player.startChat(5028)
    elif quest_stage == 4:
        player.npcChat("If you have slayed the demon, you better bring some proof!")
    else:
        player.playerChat("I better not disturb the king.")
    
def chat_5008(player):
    player.npcChat("Hello young adventurer, what brings you here?")
    player.nextChat(5009)
    
def chat_5009(player):
    player.dialogueOption("I'm looking for an adventure.", 5010, "I don't know, bye.", 5011)

def chat_5010(player):
    player.playerChat("I want to become the biggest legend in PwnXile.", "Thus I'm looking for a great adventure!")
    player.nextChat(5012)
    
def chat_5011(player):
    player.playerChat("To be honest I'm not sure, bye!")
    player.endChat()
    
def chat_5012(player):
    player.npcChat("In that case you have come to the right place.", "I have a quest that only the bravest warrior can complete", "Are you still up for the challenge young adventurer?")
    player.nextChat(5013)
    
def chat_5013(player):
    player.dialogueOption("Yes!", 5014, "No!", 5015)
    
def chat_5014(player):
    player.playerChat("Yes, of course!")
    player.nextChat(5016)
    
def chat_5015(player):
    player.playerChat("No thanks, it sounds too dangerous...")
    player.endChat()
    
def chat_5016(player):
    player.npcChat("A dangerous demon is terrorizing our great world", "To to slay this demon you must bring the Silverlight sword", "The Silverlight sword can only be made by my dwarfs.", "Bring me 10 rune bars, 20 addy bars and 100 steel bars")
    player.getQuest(3).setStage(1)
    player.refreshQuestTab()
    player.endChat()
    
def chat_5017(player):
    player.npcChat("Hand over the items, we don't have much time")
    player.deleteItem(rune_bar_id, 10)
    player.deleteItem(addy_bar_id, 20)
    player.deleteItem(steel_bar_id, 100)
    player.getQuest(3).setStage(2)
    player.refreshQuestTab()
    player.nextChat(5018)

def chat_5018(player):
    player.npcChat("The dwarfs are hungry,", "Please bring me 500 cooked manta rays!")
    player.nextChat(5019)
    
def chat_5019(player):
    player.playerChat("500 cooked manta rays!?")
    player.nextChat(5020)
    
def chat_5020(player):
    player.npcChat("The dwarfs eat a lot of food... Please hurry up!")
    player.endChat()
    
def chat_5021(player):
    player.playerChat("I have the 500 cooked manta rays now.")
    player.nextChat(5022)
    
def chat_5022(player):
    player.npcChat("Good job! Here is your Silverlight sword.")
    player.addItem(silverlight_id)
    player.deleteItem(cooked_manta_id, 500)
    player.getQuest(3).setStage(3)
    player.refreshQuestTab()
    player.nextChat(5023)
    
def chat_5023(player):
    player.npcChat("Come see me again when you are ready to fight the demon.")
    player.endChat()
    
def chat_5035(player):
    player.npcChat("Are you ready to fight the demon?")
    player.nextChat(5024)
    
def chat_5024(player):
    player.dialogueOption("Yes!", 5025, "No!", 5026)

def chat_5025(player):
    player.playerChat("Yes, take me to the demon!")
    player.nextChat(5027)
    
def chat_5026(player):
    player.playerChat("No, I'm not quite ready yet.")
    player.endChat()
    
def chat_5027(player):
    player.npcChat("As you wish young adventurer")
    player.nextChat(5050)
	
def chat_5050(player):
    player.teleport(Position.DEMONS_ROOM)
    player.endChat()
    
def chat_5028(player):
    player.playerChat("Slaying the demon was a piece of cake.")
    player.nextChat(5029)
    
def chat_5029(player):
    player.npcChat("Wha.. What? I can't believe it!")
    player.nextChat(5030)
    
def chat_5030(player):
    player.playerChat("I brought you the demon's bones as a trophy.")
    player.nextChat(5031)
    
def chat_5031(player):
    player.npcChat("Thank you " + str(player.playerName) + "!", "You will never be forgotten!")
    player.nextChat(5032)
    
def chat_5032(player):
    player.playerChat("That's it? Don't I get a reward?")
    player.nextChat(5033)
    
def chat_5033(player):
    player.npcChat("Oh... I almost forgot!")
    player.nextChat(5034)
    
def chat_5034(player):
    player.endChat()
    player.getQuest(3).setStage(5)
    player.refreshQuestTab()
    player.deleteItem(burnt_bones_id, 1)
    player.addCash(25000000)
    player.addItem(1052)
    player.getFunction().addSkillXP(500000, 10) #I DON'T KNOW IF THIS IS THE CORRECT WAY TO ADD EXP
    player.getFunction().addSkillXP(500000, 13) #I DON'T KNOW IF THIS IS THE CORRECT WAY TO ADD EXP
    player.completeQuest("Legend's Quest", "25,000,000 coins", "500,000 exp in Smithing and Fishing", "A Cape of Legends", "1 Quest Point")