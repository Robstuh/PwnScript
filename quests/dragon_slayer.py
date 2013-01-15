#This Quest was created by H E L L 0 aka Wise Old Man
#Date 14th January 2013
#Quest Length = Very Long

#Items
ned_rope_id = 954
melzar_map_id = 1535
thalzar_map_id = 1536
lozar_map_id = 1537
crandor_map_id = 1538
antidragon_shield_id = 1540
r_key_id = 1543
b_key_id = 1546
g_key_id = 1548
magic_potion_id = 3040
lobster_pot_id = 301
uncut_ruby_id = 1619
steel_nails_id = 1539

#NPCs
guildmaster_id = 198
duke_horacio_id = 741
elvarg_id = 742
klarense_id = 744
wormbrain_id = 745
oracle_id = 746
oziach_id = 747
ned_id = 918
tyras_guard_id = 1200
nechryael_id = 1613
green_dragon_id = 941
bloodvel_id = 1618
mysterious_old_man_id = 410

#Objects
dwarven_chest_id = 2995
three_key_chest_id = 2996

#Quest configuration
def configure_quest_5():
	quest_id = 5
	quest_name = 'Dragon Slayer'
	quest_stages = 23
	World.addQuest(quest_id, quest_name, quest_stages)
	World.addNonCombatNpc(guildmaster_id, 3189, 3360, 0, 0)
	World.addNonCombatNpc(oziach_id, 3069, 3517, 0, 0)
	World.addNonCombatNpc(mysterious_old_man_id, 2941, 3248, 0, 0)
	World.addNonCombatNpc(oracle_id, 3009, 3498, 0, 0)
	World.addNonCombatNpc(wormbrain_id, 3014, 3189, 0, 0)
	World.addNonCombatNpc(tyras_guard_id, 3217, 3219, 0, 0)
	World.addNonCombatNpc(duke_horacio_id, 3210, 3225, 0, 0)
	World.addNonCombatNpc(klarense_id, 3045, 3204, 0, 0)
	World.addNonCombatNpc(ned_id, 3102, 3263, 0, 1) #Location: Draynor
	#World.addNonCombatNpc(ned_id, 3047, 3204, 0, 0) #Location: Port Sarim
	World.addObject(dwarven_chest_id, 3023, 3452)
	World.addObject(three_key_chest_id, 3191, 3351)
	World.addCombatNpc(elvarg_id, 2855, 9637, 0, 1, 250, 35, 120, 120)

#Quest button
def quest_button_5(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 0:
		player.boxMessage("To start the quest, speak to the Guildmaster in the Champions' Guild.")
	elif quest_stage == 1:
		player.boxMessage("The Guildmaster told me, that Oziach will have a quest for me.")
	elif quest_stage == 2:
		player.boxMessage("Oziach said, that the Guildmaster will know what to do.")
	elif quest_stage == 3:
		player.boxMessage("I will have to find a ship and a captain for my quest.", "I should probably start looking in Port Sarim")
	elif quest_stage == 4:
		player.boxMessage("Now I have ship but I still need a captain", "Klarense suggested Ned in Draynor Village")
	elif quest_stage == 5:
		player.boxMessage("Ned accepted the challenge, but he mentioned a @dre@map to Crandor@bla@", "Maybe I should go ask the Guildmaster if he has a map.")
	elif quest_stage == 6:
		player.boxMessage("The Oracle on the Ice Mountain will know where", "to find the first part of the map")
	elif quest_stage == 7:
		player.boxMessage("To find the chest below the Oracle I will need:", "First, a drink used by a mage, Next, some yak-hair", "braided like a womans, Then, a small crustacean cage,", "Last, a red stone that's no chisel seen")
	elif quest_stage == 8:
		player.boxMessage("Bring the first part of the map to the Guildmaster", "and recieve further insctructions on your quest")
	elif quest_stage == 9:
		player.boxMessage("Wormbrain has the second part of the map, he's currently", "being hold as a prisoner in the Port Sarim Jail", "The Guildmaster said I might be able to buy the map with gold.")
	elif quest_stage == 10:
		player.boxMessage("Wormbrain will sell you the second part of the map.", "The price is 1 million gold pieces.")
	elif quest_stage == 11:
		player.boxMessage("Bring the second part of the map to the Guildmaster", "and recieve further insctructions on your quest")
	elif quest_stage == 12:
		player.boxMessage("The first type of monsters I have to kill is @dre@Nechryaels@bla@.")
	elif quest_stage == 13:
		player.boxMessage("The second type of monsters I have to kill is @dre@Bloodvels@bla@.")
	elif quest_stage == 14:
		player.boxMessage("The third type of monsters I have to kill is @dre@Green Dragons@bla@.")
	elif quest_stage == 15:
		player.boxMessage("I should probably return to the Guildmanster with the keys.")
	elif quest_stage == 16:
		player.boxMessage("The last part of the map is on the other side", "of the Champion's Guild.")
	elif quest_stage == 17:
		player.boxMessage("Bring the last part of the map to the Guildmaster", "and recieve further insctructions on your quest")
	elif quest_stage == 18:
		player.boxMessage("Travel to @dre@Port Sarim@bla@ and check if your ship is ready.")
	elif quest_stage == 19:
		player.boxMessage("I'll have to bring 200 steel nails and 5 ropes to Klarense.")
	elif quest_stage == 20:
		player.boxMessage("My ship is ready soon, I should perhaps inform to the Guildmaster.")
	elif quest_stage == 21:
		player.boxMessage("Duke Horacio in Lumbridge will give me a free @dre@anti-dragon shield@bla@.")
	elif quest_stage == 22:
		player.boxMessage("I'm ready to fight Elvarg I should go speak to Klarense")
	elif quest_stage == 23:
		player.boxMessage("I have completed @dre@Dragon Slayer@bla@.")

#Guildmaster
def first_click_npc_198(player):
	total_level = player.getTotalLevel()
	quest_points = player.getQuestPoints()
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 0 and quest_points < 3 and total_level < 1699:
		player.boxMessage("You need to have at least 4 quest points", "and a total level of 1700 or higher", "to start the quest @dre@Dragon Slayer@bla@.")
	elif quest_stage == 0 and quest_points > 3:
		player.startChat(7100)
	elif quest_stage == 2:
		player.startChat(7138)
	elif quest_stage == 5:
		player.startChat(7198)
	elif quest_stage == 8 and player.hasItem(thalzar_map_id):
		player.startChat(7213)
	elif quest_stage == 8 and not player.hasItem(thalzar_map_id):
		player.playerChat("I should probably bring the map", "before speaking to the Guildmaster.")
	elif quest_stage == 11 and player.hasItem(lozar_map_id):
		player.startChat(7242)
	elif quest_stage == 11 and not player.hasItem(lozar_map_id):
		player.playerChat("I should probably bring the map", "before speaking to the Guildmaster.")
	elif quest_stage == 15 and player.hasItem(r_key_id) and player.hasItem(b_key_id) and player.hasItem(g_key_id):
		player.startChat(7249)
	elif quest_stage == 15:
		player.playerChat("I should bring the 3 keysbefore speaking", " to the Guildmaster.")
	elif quest_stage == 17 and player.hasItem(melzar_map_id):
		player.startChat(7253)
	elif quest_stage == 17:
		player.playerChat("I should probably bring the map before speaking to the Guildmaster.")
	elif quest_stage == 20:
		player.startChat(7266)
	else:
		player.playerChat("I better not disturb the Guildmaster right now")

#Oziach
def first_click_npc_747(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 1:
		player.startChat(7111)
	else:
		player.playerChat("Maybe I should just leave this house...")

#Klarense
def first_click_npc_744(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 3 and player.hasItem(995, 5000000):
		player.startChat(7158)
	elif quest_stage == 3 and not player.hasItem(995, 5000000):
		player.playerChat("The sign says 5,000,000 gold pieces", "I better get the gold before I disturb")
	elif quest_stage == 18:
		player.startChat(7259)
	elif quest_stage == 19 and player.hasItem(steel_nails_id, 200) and player.hasItem(ned_rope_id, 5):
		player.startChat(7264)
	elif quest_stage == 19 and not player.hasItem(steel_nails_id, 200) and not player.hasItem(ned_rope_id, 5):
		player.playerChat("I must have 200 steel nails and 5 ropes before speaking to Klarense.")
	else:
		player.npcChat("Leave me alone!")

#Ned
def first_click_npc_918(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage < 4:
		player.startChat(7172)
	elif quest_stage == 4:
		player.startChat(7175)
	elif quest_stage == 22:
		player.startChat(7293)
	else:
		player.sendMessage("Ned looks confused, better leave him be.")
		
#Oracle
def first_click_npc_746(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 6:
		player.startChat(7207)
	else:
		player.playerChat("I'd rather not talk to the Oracle right now.")

#Wormbrain
def first_click_npc_745(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 9:
		player.startChat(7222)
	elif quest_stage == 10 and player.hasItem(995, 1000000):
		player.startChat(7235)
	elif quest_stage == 10 and not player.hasItem(995, 1000000):
		player.playerChat("I need 1 million gold pieces before talking to him again")
	else:
		player.playerChat("I don't want to disturb the goblin...")

#Tyras Guard
def first_click_npc_1200(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 21:
		player.startChat(7274)
	else:
		player.playerChat("Wonder what he's guarding?")

#Duke Horacio
def first_click_npc_741(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 21:
		player.startChat(7278)
	else:
		player.playerChat("Duke Horacio looks busy right now.")

#Chest
def first_click_object_2995(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 7 and player.hasItem(ned_rope_id) and player.hasItem(uncut_ruby_id) and player.hasItem(lobster_pot_id) and player.hasItem(magic_potion_id):
		player.boxMessage("You open the chest and find a part of a map.", "It'll probably be best to give it to the Guildmaster")
		player.deleteItem(ned_rope_id, 1)
		player.deleteItem(uncut_ruby_id, 1)
		player.deleteItem(lobster_pot_id, 1)
		player.deleteItem(magic_potion_id, 1)
		player.addItem(thalzar_map_id)
		player.sendMessage("@dre@You have recieved the first part of the map.@bla@")
		player.getQuest(5).setStage(8)
	elif quest_stage == 7:
		player.boxMessage("You don't have the required items to open the chest.")
	else:
		player.boxMessage("The chest is empty.")

#Chest2
def first_click_object_2996(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 16 and player.hasItem(r_key_id) and player.hasItem(b_key_id) and player.hasItem(g_key_id):
		player.boxMessage("You open the chest and find a piece of a map.", "It'll probably be best to give it to the Guildmaster")
		player.deleteItem(g_key_id, 1)
		player.deleteItem(b_key_id, 1)
		player.deleteItem(g_key_id, 1)
		player.addItem(melzar_map_id)
		player.sendMessage("@dre@You have recieved the last part of the map.@bla@")
		player.getQuest(5).setStage(17)
	elif quest_stage == 16:
		player.boxMessage("You need all 3 keys to open the chest.")
	else:
		player.boxMessage("The chest is empty...")
		
#Nechryael slaying
def kill_npc_1613(player):
    if player.hasAttribute("nechryael_kills"):
        handle_nechryael_kill(player)
    else:
        player.addAttribute("nechryael_kills", 1)
        
def handle_nechryael_kill(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 12 and player.getAttribute("nechryael_kills") > 19:
		player.addAttribute("nechryael_kills", 0)
		player.sendMessage("You have received a red key.")
		player.addItem(r_key_id)
		player.getQuest(5).setStage(13)
	else:
		player.addAttribute("nechryael_kills", player.getAttribute("nechryael_kills") + 1)
        
#Bloodvel slaying
def kill_npc_1618(player):
	if player.hasAttribute("bloodvel_kills"):
		handle_bloodvel_kill(player)
	else:
		player.addAttribute("bloodvel_kills", 1)
        
def handle_bloodvel_kill(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 13 and player.getAttribute("bloodvel_kills") > 24:
		player.addAttribute("bloodvel_kills", 0)
		player.sendMessage("You have received a blue key.")
		player.addItem(b_key_id)
		player.getQuest(5).setStage(14)
	else:
		player.addAttribute("bloodvel_kills", player.getAttribute("bloodvel_kills") + 1)
        
#Green dragon slaying
def kill_npc_941(player):
	if player.hasAttribute("gdragon_kills"):
		handle_gdragon_kill(player)
	else:
		player.addAttribute("gdragon_kills", 1)

def command_cheat(player):
	player.getQuest(5).setStage(15)

def handle_gdragon_kill(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 14 and player.getAttribute("gdragon_kills") > 17:
		player.addAttribute("gdragon_kills", 0)
		player.sendMessage("You have received a green key.")
		player.addItem(g_key_id)
		player.boxMessage("I should probably return to the Guildmanster with the keys.")
		player.getQuest(5).setStage(15)
	else:
		player.addAttribute("gdragon_kills", player.getAttribute("gdragon_kills") + 1)

#Elvarg
def kill_npc_742(player):
	quest_stage = player.getQuest(5).getStage()
	if quest_stage == 22:
		player.getQuest(5).setStage(23)
		player.completeQuest("Dragon Slayer", "Ability to equip a Dragonfire Shield", "3 Quest Points", " ", " ",)
		player.qp += 2 # an extra 2 quest points 

def chat_7100(player):
	player.npcChat("Greetings!")
	player.nextChat(7101)
	
def chat_7101(player):
	player.dialogueOption("What is this place?", 7102, "Can I have a quest?", 7104)
	
def chat_7102(player):
	player.playerChat("What is this place, and who're you?")
	player.nextChat(7103)

def chat_7103(player):
	player.npcChat("You're in the champions guild and I am the Guildmaster!")
	player.endChat()

def chat_7104(player):
	player.playerChat("Can I have a quest?")
	player.nextChat(7105)

def chat_7105(player):
	player.npcChat("Aha!")
	player.nextChat(7106)

def chat_7106(player):
	player.npcChat("Yes! A mighty and perilous quest fit only for the most",
				   "powerful champions! And, at the end of it, you will earn",
				   "the right to wear the legendary rune platebody!")
	player.nextChat(7107)

def chat_7107(player):
	player.playerChat("So, what is this quest?")
	player.nextChat(7108)

def chat_7108(player):
	player.npcChat("You'll have to speak to Oziach, the maker of rune",
				   "armour. He sets the quests that champions must",
				   "complete in order to wear it.")
	player.nextChat(7109)

def chat_7109(player):
	player.playerChat("Where do I find this Oziach?")
	player.nextChat(7110)

def chat_7110(player):
	player.npcChat("Oziach lives in a hut, by the cliffs to the west of", "Edgeville. He can be a little...odd...sometimes, though.")
	player.getQuest(5).setStage(1)
	player.refreshQuestTab()
	player.endChat()

def chat_7111(player):
	player.npcChat("Aye, 'tis a fair day my friend.")
	player.nextChat(7112)

def chat_7112(player):
	player.dialogueOption("Can you sell me a rune platebody?", 7113, "I'm not your friend", 7128, "Yes, it's a very nice day.", 7130)

def chat_7113(player):
	player.playerChat("Can you sell me a rune platebody?")
	player.nextChat(7114)

def chat_7114(player):
	player.npcChat("So, how does thee know I 'ave some?")
	player.nextChat(7115)

def chat_7115(player):
	player.playerChat("The Guildmaster of the Champions' Guild told me.")
	player.nextChat(7116)

def chat_7116(player):
	player.npcChat("Yes, I suppose he would, wouldn't he? He's always", 
				   "sending you fancy-pants 'heroes' up to bother me.", 
				   "Telling me I'll give them a quest or sommat like that.")
	player.nextChat(7117)

def chat_7117(player):
	player.npcChat("Well, I'm not just going to let anyone wear my rune", 
				   "platemail. It's only for heroes. So, leave me alone.")
	player.nextChat(7118)

def chat_7118(player):
	player.dialogueOption("I thought you were going to give me a quest.", 7119, "That's a pity, I'm not a hero.", 7132)

def chat_7119(player):
	player.playerChat("I thought you were going to give me a quest...")
	player.nextChat(7120)

def chat_7120(player):
	player.npcChat("*Sigh*")
	player.nextChat(7121)

def chat_7121(player):
	player.npcChat("All right, I'll give ye a quest. I'll let you wear my rune", 
				   "platemail if ye...")
	player.nextChat(7122)

def chat_7122(player):
	player.npcChat("Slay the dragon of Crandor!")
	player.nextChat(7123)

def chat_7123(player):
	player.dialogueOption("A dragon, that sounds like fun.", 7124, "I may be a champion, but I'm not up for dragon-killing yet.", 7133)

def chat_7124(player):
	player.playerChat("A dragon, that sounds like fun.")
	player.nextChat(7125)

def chat_7125(player):
	player.npcChat("Hah, yes, you are a typical reckless adventurer, aren't", 
				   "you? Now go kill the dragon and get out of my face.")
	player.nextChat(7126)

def chat_7126(player):
	player.playerChat("But how can I defeat the dragon?")
	player.nextChat(7127)

def chat_7127(player):
	player.npcChat("Go talk to the Guildmaster in the Champions' Guild. He'll", "help you out if yer so keen on doing a quest. I'm not", "going to be handholding any adventurers.")
	player.getQuest(5).setStage(2)
	player.endChat()

def chat_7128(player):
	player.playerChat("I'm not your friend!")
	player.nextChat(7129)

def chat_7129(player):
	player.npcChat("Then get yer ass outa here!")
	player.endChat()

def chat_7130(player):
	player.playerChat("Yes, it's a very nice day.")
	player.nextChat(7131)

def chat_7131(player):
	player.npcChat("Why are ye here?")
	player.nextChat(7113)

def chat_7132(player):
	player.playerChat("That's a pity, I'm not a hero.")
	player.endChat()

def chat_7133(player):
	player.playerChat("I may be a champion, but I'm not up for dragon-killing yet.")
	player.nextChat(7134)

def chat_7134(player):
	player.npcChat("Are ye sure ye wanna walk away?")
	player.nextChat(7135)

def chat_7135(player):
	player.dialogueOption("Yes.", 7136, "No.", 7137)

def chat_7136(player):
	player.playerChat("Yes, I'm leaving you alone for now.")
	player.endChat()

def chat_7137(player):
	player.playerChat("No, actually a dragon sounds like fun.")
	player.nextChat(7125)

def chat_7138(player):
	player.dialogueOption("What is this place?", 7102, "I talked to Oziach...", 7139)
	player.nextChat(71)

def chat_7139(player):
	player.playerChat("I talked to Oziach...")
	player.nextChat(7140)

def chat_7140(player):
	player.npcChat("Oh? What did he tell you to do?")
	player.nextChat(7141)

def chat_7141(player):
	player.playerChat("Defeat the dragon of Crandor.")
	player.nextChat(7142)

def chat_7142(player):
	player.npcChat("The dragon of Crandor?")
	player.nextChat(7143)

def chat_7143(player):
	player.playerChat("Um, yes...")
	player.nextChat(7144)

def chat_7144(player):
	player.npcChat("Goodness, he hasn't given you an easy job, has he?")
	player.nextChat(7145)

def chat_7145(player):
	player.playerChat("What's so special about this dragon?")
	player.nextChat(7146)

def chat_7146(player):
	player.npcChat("Thirty years ago, Crandor was a thriving community", 
				   "with a great tradition of mages and adventurers. Many", 
				   "Crandorians even earned the right to be a part of the", 
				   "Champions' Guild!")
	player.nextChat(7147)

def chat_7147(player):
	player.npcChat("One of their adventurers went too far, however. He", 
				   "descended in to the volcano of the centre of Crandor", 
				   "and woke the dragon Elvarg.")
	player.nextChat(7148)

def chat_7148(player):
	player.npcChat("He must have fought valiantly against the dragon", 
				   "because they say that, to this day, she has a scar down", 
				   "her side,")
	player.nextChat(7149)

def chat_7149(player):
	player.npcChat("but the dragon still won the fight. She emerged and laid", 
				   "waste to the whole of Crandor with her fire breath!")
	player.nextChat(7150)

def chat_7150(player):
	player.npcChat("If you're serious about taking on Elvarg, first you'll", 
				   "need to get to Crandor. The island is surrounded by", 
				   "dangerous reefs, so you'll need a ship capable of getting", 
				   "through them and a captain that knows the way.")
	player.nextChat(7151)

def chat_7151(player):
	player.dialogueOption("Where can I find a ship and a captain to Crandor?", 7152, "Maybe I shouldn't do this quest", 0)

def chat_7152(player):
	player.playerChat("Where can I find a captain that will sail to Crandor?")
	player.nextChat(7153)

def chat_7153(player):
	player.npcChat("I would start at Port Sarim, there are plenty of captains", 
				   "around there that you might be able to convince to", 
				   "sail you to Crandor.")
	player.nextChat(7154)

def chat_7154(player):
	player.playerChat("Where can I find the right ship?")
	player.nextChat(7155)

def chat_7155(player):
	player.npcChat("Even if you find a captian to take you, only a ship", 
				   "made to the old crandorian design would be able to", 
				   "navigate through the reefs to the island.")
	player.nextChat(7156)

def chat_7156(player):
	player.npcChat("If there's still one in existence, it's probably in Port", 
				   "Sarim.")
	player.nextChat(7157)

def chat_7157(player):
	player.getQuest(5).setStage(3)
	player.npcChat("Then, of course, you'll need to find a captain willing to", "sail to Crandor, and I'm not sure where you'd find one", "of them!")
	player.endChat()

def chat_7158(player):
	player.dialogueOption("I heard your ship is for sail?", 7160, "Nevermind.", 7159)

def chat_7159(player):
	player.playerChat("Nevermind.")
	player.endChat()

def chat_7160(player):
	player.npcChat("So, are you interested in buying the ship? Now, I'll be", 
				   "straight with you: she's not quite seaworthy right now,", 
				   "but if you purchase her I'll give her some work and", 
				   "she'll be the nippiest ship this side of Port Khazard.")
	player.nextChat(7161)

def chat_7161(player):
	player.dialogueOption("Would you take me to Crandor when she's ready", 7162, "I'd like to buy her.", 7168, "Ah well, never mind.", 7159)

def chat_7162(player):
	player.playerChat("Would you take me to Crandor when she's ready")
	player.nextChat(7163)

def chat_7163(player):
	player.npcChat("Crandor? You're joking, right?")
	player.nextChat(7164)

def chat_7164(player):
	player.playerChat("No. I want to go to Crandor.")
	player.nextChat(7165)

def chat_7165(player):
	player.npcChat("Then you must be crazy.")
	player.nextChat(7166)

def chat_7166(player):
	player.npcChat("That island is surrounded by reefs that would rip this", 
				   "ship to shreds. You'd need an experienced captain to", 
				   "stand a change of getting through.")
	player.nextChat(7167)

def chat_7167(player):
	player.npcChat("And, even if I could get to it, there's no way I'm going", 
				   "any closer to that dragon than I have to. You could try", 
				   "to ask Ned in Draynor Village, he was once a captain.")
	player.nextChat(7161)

def chat_7168(player):
	player.playerChat("I'd like to buy her.")
	player.nextChat(7169)

def chat_7169(player):
	player.npcChat("How does 5,000,000 gold sound? I'll even throw in my", 
				   "cabin boy, Jenkins, for free! He'll swab the decks and", 
				   "splice the mainsails for you!")
	player.nextChat(7170)

def chat_7170(player):
	player.playerChat("Yep, sounds good.")
	player.nextChat(7171)

def chat_7171(player):
	player.getQuest(5).setStage(4)
	player.npcChat("Okey dokey, she's all yours!")
	player.nextChat(7161)

def chat_7172(player):
	player.npcChat("Why, hello there, lass. Me friends call me Ned. I was a", 
				   "man of the sea, it's past me now. Could I be", 
				   "making or selling you some rope?")
	player.nextChat(7173)

def chat_7173(player):
	player.playerChat("You're a sailor? Could you take me to Crandor?")
	player.nextChat(7174)

def chat_7174(player):
	player.npcChat("I'll think about it, come ask me again when you have a boat.")
	player.endChat()

def chat_7175(player):
	player.npcChat("Why, hello there, lass. Me friends call me Ned. I was a", 
				   "man of the sea, it's past me now. Could I be", 
				   "making or selling you some rope?")
	player.nextChat(7176)

def chat_7176(player):
	player.dialogueOption("You're a sailor? Could you take me to Crandor?", 7180, "Yes, I would like some rope.", 7177, "No thanks, Ned, I don't need any.", 7179)
	player.nextChat(71)

def chat_7177(player):
	player.playerChat("Yes, I would like some rope.")
	player.nextChat(7178)

def chat_7178(player):
	player.addItem(ned_rope_id, 1)
	player.npcChat("Here's your rope me friend.")
	player.endChat()

def chat_7179(player):
	player.playerChat("No thanks, Ned, I don't need any.")
	player.endChat()

def chat_7180(player):
	player.playerChat("You're a sailor? Could you take me to Crandor?")
	player.nextChat(7181)

def chat_7181(player):
	player.npcChat("Well, I was a sailor. I've not been able to get work at", 
				   "sea these days, though. They say I'm too old.")
	player.nextChat(7182)

def chat_7182(player):
	player.npcChat("Sorry, where was it you said you wanted to go?")
	player.nextChat(7183)

def chat_7183(player):
	player.playerChat("To the island of Crandor.")
	player.nextChat(7184)

def chat_7184(player):
	player.npcChat("Crandor?")
	player.nextChat(7185)

def chat_7185(player):
	player.npcChat("But... It would be a chance to sail a ship once more.", 
				   "I'd sail anywhere if it was a chance to sail again.")
	player.nextChat(7186)

def chat_7186(player):
	player.npcChat("Then again, no captain in his right mind would sail to", 
				   "that island.")
	player.nextChat(7187)

def chat_7187(player):
	player.npcChat("Ah, you only live once! I'll do it!")
	player.nextChat(7188)

def chat_7188(player):
	player.npcChat("So, where's your ship?")
	player.nextChat(7189)

def chat_7189(player):
	player.playerChat("It's the Lady Lumbridge, in Port Sarim.")
	player.nextChat(7190)

def chat_7190(player):
	player.npcChat("That old pile of junk? Last I heard, she wasn't", 
				   "seaworthy.")
	player.nextChat(7191)

def chat_7191(player):
	player.playerChat("I'm getting her fixed up.")
	player.nextChat(7192)

def chat_7192(player):
	player.npcChat("You are? Excellent! Come meet me here when", 
				   "she's fixed and bring your map to Crandor.")
	player.nextChat(7193)

def chat_7193(player):
	player.playerChat("My map to Crandor?")
	player.nextChat(7194)

def chat_7194(player):
	player.npcChat("Ay, you do have a map right?")
	player.nextChat(7195)

def chat_7195(player):
	player.getQuest(5).setStage(5)
	player.playerChat("Yes, of course I have a map!")
	player.endChat()

def chat_7196(player):
	player.npcChat("Why, hello there, lass. Me friends call me Ned. I was a", 
				   "man of the sea, it's past me now. Could I be", 
				   "making or selling you some rope?")
	player.nextChat(7197)

def chat_7197(player):
	player.dialogueOption("Yes, I would like some rope.", 7177, "No thanks, Ned, I don't need any.", 7179)

def chat_7198(player):
	player.dialogueOption("What is this place?,", 7103, "About my quest to kill the dragon...", 7199)
	player.nextChat(7199)

def chat_7199(player):
	player.playerChat("I've found myself a captain and a boat!")
	player.nextChat(7200)

def chat_7200(player):
	player.npcChat("Good job job " + str(player.playerName) + "!", "Now you're ready for the next part")
	player.nextChat(7201)

def chat_7201(player):
	player.playerChat("The next part? Ned mentioned a map to Crandor,", "is that the next part?")
	player.nextChat(7202)

def chat_7202(player):
	player.npcChat("Yes my friend, that's the next part of your quest.")
	player.nextChat(7203)

def chat_7203(player):
	player.npcChat("There is only one map left in all of PwnXile,", 
				   "but when the dragon took over Crandor,", 
				   "the map got ripped in to three parts")
	player.nextChat(7204)

def chat_7204(player):
	player.playerChat("Where do I find the first part of the map?")
	player.nextChat(7205)

def chat_7205(player):
	player.npcChat("Only the Oracle on the Ice Mountain", "would know where it is.")
	player.nextChat(7206)

def chat_7206(player):
	player.getQuest(5).setStage(6)
	player.playerChat("Alright, bye.")
	player.endChat()

def chat_7207(player):
	player.dialogueOption("Will you help me find a part of the map to Crandor?", 7208, "Nevermind.", 7159)

def chat_7208(player):
	player.playerChat("Will you help me find the first part of", "the map to Crandor?")
	player.nextChat(7209)

def chat_7209(player):
	player.npcChat("The map's in a chest below,", "but opening is rather tough." "This is what you need to know,", "You must use the following stuff:")
	player.nextChat(7210)

def chat_7210(player):
	player.npcChat("First, a drink used by a mage, Next, some yak-hair", "braided like a womans, Then, a small crustacean cage,", "Last, a red stone that's no chisel seen.")
	player.nextChat(7211)

def chat_7211(player):
	player.playerChat("wat")
	player.nextChat(7212)

def chat_7212(player):
	player.npcChat("First, a drink used by a mage, Next, some yak-hair",
	"braided like a womans, Then, a small crustacean cage,", 
	"Last, a red stone that's no chisel seen.")
	player.getQuest(5).setStage(7)
	player.endChat()

def chat_7213(player):
	player.dialogueOption("What is this place?", 7103, "About my quest to kill the dragon...", 7214)

def chat_7214(player):
	player.playerChat("I found the first part of the map!")
	player.nextChat(7215)

def chat_7215(player):
	player.npcChat("Good job! Now you'll just have to find two more parts.", "I'll hold on to the first part of the map for you meanwhile.")
	player.deleteItem(thalzar_map_id, 1)
	player.sendMessage("@You give the first part of the map to the Guildmaster.")
	player.nextChat(7216)

def chat_7216(player):
	player.playerChat("Sooo, where's the next part if I may ask?")
	player.nextChat(7217)

def chat_7217(player):
	player.npcChat("The next part of the map was Lozar's.", 
				   "Unfortunately, she was killed during a goblin raid,", 
				   "the creatures looting everything from the homes.")
	player.nextChat(7218)

def chat_7218(player):
	player.npcChat("The second map piece is in the possession of a goblin", 
				   "named Wormbrain, who is being held in the Port Sarim Jail.")
	player.nextChat(7219)

def chat_7219(player):
	player.playerChat("Good! I'll just go kill the creature then!")
	player.nextChat(7220)

def chat_7220(player):
	player.npcChat("I've heard Wormbrain likes gold, you could", 
				   "just buy the map from him instead.")
	player.nextChat(7221)

def chat_7221(player):
	player.playerChat("Alright, I'll go get the second part now...")
	player.getQuest(5).setStage(9)
	player.endChat()

def chat_7222(player):
	player.playerChat("Do you have the second part of the map to Crandor!")
	player.nextChat(7223)

def chat_7223(player):
	player.npcChat("...")
	player.nextChat(7224)

def chat_7224(player):
	player.playerChat("ANSWER ME!")
	player.nextChat(7225)

def chat_7225(player):
	player.npcChat("Why should I give the map to you human?")
	player.nextChat(7226)

def chat_7226(player):
	player.playerChat("... I'll kill you!")
	player.nextChat(7227)

def chat_7227(player):
	player.npcChat("Just do that... I don't care...")
	player.nextChat(7228)

def chat_7228(player):
	player.playerChat("What if I gave you gold?")
	player.nextChat(7229)

def chat_7229(player):
	player.npcChat("Gold?")
	player.nextChat(7230)

def chat_7230(player):
	player.playerChat("Yes, piles of gold!")
	player.nextChat(7231)

def chat_7231(player):
	player.npcChat("I'll sell it to you for 1 billion gold pieces!")
	player.nextChat(7232)

def chat_7232(player):
	player.playerChat("Perhaps I should just walk away.")
	player.nextChat(7233)

def chat_7233(player):
	player.npcChat("No wait! What about 1 million gold pieces? Please human.")
	player.nextChat(7234)

def chat_7234(player):
	player.getQuest(5).setStage(10)
	player.playerChat("Okay, I'll come back with 1 million gold pieces,", 
	"and you better have the map, or I swear",
	"I'll take your meaningless life instead")
	player.endChat()

def chat_7235(player):
	player.playerChat("I've brought 1 million gold pieces.")
	player.nextChat(7236)

def chat_7236(player):
	player.npcChat("Good, give them to me.")
	player.nextChat(7237)

def chat_7237(player):
	player.playerChat("Alright, here's your gold.")
	player.deleteItem(995, 1000000)
	player.nextChat(7238)

def chat_7238(player):
	player.playerChat("Now give me my map!")
	player.nextChat(7239)

def chat_7239(player):
	player.npcChat("No, go away!")
	player.nextChat(7240)

def chat_7240(player):
	player.playerChat("Okay, then I'll have to kill you, and you won't", "have any of the million gold pieces anymore!")
	player.nextChat(7241)

def chat_7241(player):
	player.addItem(lozar_map_id)
	player.sendMessage("@dre@You have recieved the second part of the map.@bla@")
	player.getQuest(5).setStage(11)
	player.npcChat("Okay here's your map, please don't kill me!")
	player.endChat()

def chat_7242(player):
	player.playerChat("I have the second part of the map now!")
	player.nextChat(7243)

def chat_7243(player):
	player.npcChat("Great job, now there's only one part of the map left!")
	player.nextChat(7244)

def chat_7244(player):
	player.npcChat("The last part of the map can also be found in a chest.", "But to open the chest you'll need 3 colored keys.")
	player.nextChat(7245)

def chat_7245(player):
	player.playerChat("Where do I get these keys, and where's the chest located?")
	player.nextChat(7246)

def chat_7246(player):
	player.npcChat("To get the keys you will have to kill three", "different types of monsters")
	player.nextChat(7247)

def chat_7247(player):
	player.npcChat("To get the keys kill the following monsters:", 
				   "It's important to kill them in this exact order.", 
				   "Nechryaels, Bloodvels and Green Dragons.")
	player.nextChat(7248)

def chat_7248(player):
	player.deleteItem(lozar_map_id, 1)
	player.sendMessage("@dre@You have gave the second part of the map to the Guildmaster.@bla@")
	player.getQuest(5).setStage(12)
	player.npcChat("Give me the second part of the map, and start killing!")
	player.endChat()

def chat_7249(player):
	player.dialogueOption("What is this place?", 7103, "I got all 3 keys now where's the chest?", 7250)
	player.nextChat(7250)

def chat_7250(player):
	player.npcChat("Very good " + str(player.playerName) + ".", "I was almost beginning to think you got killed.")
	player.nextChat(7251)

def chat_7251(player):
	player.playerChat("Where is the last chest if I may ask?")
	player.nextChat(7252)

def chat_7252(player):
	player.npcChat("The chest is on the other side of my Guild", "I've been guarding it for many years.", "Go get the last part of the map and then return here.")
	player.getQuest(5).setStage(16)
	player.endChat()

def chat_7253(player):
	player.playerChat("I finally have the last part of the map, what now?")
	player.nextChat(7254)

def chat_7254(player):
	player.npcChat("Travel to Port Sarim, and see if your ship is fixed.", "When the ship is fixed you're ready to fight Elvarg!")
	player.nextChat(7255)

def chat_7255(player):
	player.playerChat("Don't you forget something?")
	player.nextChat(7256)

def chat_7256(player):
	player.npcChat("And what would that be?")
	player.nextChat(7257)

def chat_7257(player):
	player.playerChat("The last part of the map...")
	player.nextChat(7258)

def chat_7258(player):
	player.npcChat("Oh yes of course,", "give it to me and you can have the full map.", "And then go check if your ship is fixed!")
	player.deleteItem(melzar_map_id)
	player.addItem(crandor_map_id)
	player.sendMessage("@dre@You have received a map of Crandor@bla@")
	player.getQuest(5).setStage(18)
	player.endChat()

def chat_7259(player):
	player.playerChat("Hello again, is she fixed yet?")
	player.nextChat(7260)

def chat_7260(player):
	player.npcChat("I've run into some problems, and I'll need your help...")
	player.nextChat(7261)

def chat_7261(player):
	player.playerChat("What's wrong? She looks fine to me.")
	player.nextChat(7262)

def chat_7262(player):
	player.npcChat("She's not fine. I'll need you to bring me some materials.", 
				   "I need you to bring me @dre@200 steel nails and 5 ropes.")
	player.nextChat(7263)

def chat_7263(player):
	player.playerChat("Alright, see you later.")
	player.getQuest(5).setStage(19)
	player.endChat()

def chat_7264(player):
	player.playerChat("I got the nails and ropes for you.")
	player.nextChat(7265)

def chat_7265(player):
	player.npcChat("Good job, the ship will be ready to sail when you need it.")
	player.getQuest(5).setStage(20)
	player.deleteItem(954, 5)
	player.deleteItem(1539, 200)
	player.endChat()

def chat_7266(player):
	player.dialogueOption("What is this place?", 7103, "About my quest to kill the dragon...", 7267)

def chat_7267(player):
	player.playerChat("My ship is ready soon, can I fight the dragon now?")
	player.nextChat(7268)

def chat_7268(player):
	player.npcChat("Do you have an anti-dragon shield?")
	player.nextChat(7269)

def chat_7269(player):
	player.playerChat("No what is that?")
	player.nextChat(7270)

def chat_7270(player):
	player.npcChat("The anti-dragon shield will absorb the dragon's fire.", "Without it you will die a painful death.")
	player.nextChat(7271)

def chat_7271(player):
	player.playerChat("And where do I get a shield like this?")
	player.nextChat(7272)

def chat_7272(player):
	player.npcChat("Travel to Lumbridge and speak to Duke Horacio, he'll give", 
				   "you a free shield, and then you'll be ready to the dragon!")
	player.nextChat(7273)
	player.getQuest(5).setStage(21)

def chat_7273(player):
	player.playerChat("Alright, see you when Elvarg is dead!")
	player.endChat()

def chat_7274(player):
	player.playerChat("May I please enter the castle?")
	player.nextChat(7275)

def chat_7275(player):
	player.npcChat("What do you want here?")
	player.nextChat(7276)

def chat_7276(player):
	player.playerChat("I wish to see Duke Horacio, I need an anti-dragon shield.")
	player.nextChat(7277)

def chat_7277(player):
	player.npcChat("Alright, follow me.")
	player.move(3210, 3224, 0)
	player.endChat()

def chat_7278(player):
	player.npcChat("Greetings. Welcome to my castle.")
	player.nextChat(7279)

def chat_7279(player):
	player.dialogueOption("I seek a shield that will protect me from dragonbreath.", 7280, "Nevermind.", 7159)

def chat_7280(player):
	player.playerChat("I seek a shield that will protect me from dragonbreath.")
	player.nextChat(7281)

def chat_7281(player):
	player.npcChat("A knight going on a dragon quest, hmm?", 
				   "What dragon do you intend to slay?")
	player.nextChat(7282)

def chat_7282(player):
	player.dialogueOption("Elvarg, the dragon of Crandor island!", 7283, "Oh, no dragon in particular.", 0)

def chat_7283(player):
	player.playerChat("Elvarg, the dragon of Crandor island!")
	player.nextChat(7284)

def chat_7284(player):
	player.npcChat("Elvarg? Are you sure?")
	player.nextChat(7285)

def chat_7285(player):
	player.playerChat("Yes.")
	player.nextChat(7286)

def chat_7286(player):
	player.npcChat("Well, you're a braver adventurer than I!")
	player.nextChat(7287)

def chat_7287(player):
	player.playerChat("Why is everyone so scared of this dragon?")
	player.nextChat(7288)

def chat_7288(player):
	player.npcChat("Back in my father's day, Crandor was an important", 
				   "city-state. Politically, it was as important as Falador or", 
				   "Varrock and its ships traded with every port.")
	player.nextChat(7289)

def chat_7289(player):
	player.npcChat("But, one day when I was little, all contact was lost. The", 
				   "trading ships and the diplomatic envoys just stopped", 
				   "coming.")
	player.nextChat(7290)

def chat_7290(player):
	player.npcChat("lookouts on the roof to warn if the dragon was", 
				   "approaching. All the city rulers were worried that", 
				   "Elvarg would devastate the whole continent.")
	player.nextChat(7291)

def chat_7291(player):
	player.playerChat("So, are you going to give me the shield or not?")
	player.nextChat(7292)

def chat_7292(player):
	player.npcChat("If you really think you're up to it then perhaps you", 
				   "are the one who can kill this dragon.")
	player.sendMessage("@dre@The Duke hands you a heavy orange shield.@bla@")
	player.addItem(antidragon_shield_id)
	player.getQuest(5).setStage(22)
	player.endChat()

def chat_7293(player):
	player.playerChat("I'm ready to sail now!")
	player.nextChat(7294)

def chat_7294(player):
	player.npcChat("Are you sure?")
	player.nextChat(7295)

def chat_7295(player):
	player.dialogueOption("Yes", 7296, "No", 0)

def chat_7296(player):
	player.npcChat("Ay ay, let's sail!")
	player.endChat()
	player.getTask().movePlayerCutscene(2850, 9637, 0)