#==============================================================================
#title           : 
#description     : 
#author          : 
#date            :
#version         :
#notes           :
#==============================================================================

monkeys_uncle_id = 1453

def configure_quest_2():
	quest_id = 2 # unique id for quest
	quest_name = 'Nut Hunt II' # name of quest
	quest_stages = 2 # final stage id when quest is completed
	World.addQuest(quest_id, quest_name, quest_stages)
	
def quest_button_2(player):
	player.boxMessage(" ")