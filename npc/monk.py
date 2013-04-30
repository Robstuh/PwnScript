from com.pwnxile.core import World
# NPC Config Script
# Monk - 222
# Author Robbie

monk_id = 222
monk_1 = World.addCombatNpc(monk_id, 3053, 3489, 0, 1, 50, 40, 150, 150)
monk_2 = World.addCombatNpc(monk_id, 3051, 3491, 0, 1, 50, 40, 150, 150)

def command_start(p):
    monk_1.attackNpc(monk_2, 30, 369, 1979) # attack using ice barrage xd

def first_click_npc_222(player):
    player.startChat(2105)
    
def chat_2105(player):
    player.playerChat("Hello there!")
    player.nextChat(2106)

def chat_2106(player):
    player.npcChat("Greetings!", "Welcome to the Monastery.")
    player.nextChat(2107)

def chat_2107(player):
    player.playerChat("Thanks!")
    player.endChat()
