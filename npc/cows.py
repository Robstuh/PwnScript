# NPC Config Script
# Cow - 81
# Author Robbie

def kill_npc_81(player):
	if player.hasAttribute("cow_kills"):
		handle_cow_kill(player)
	else:
		player.addAttribute("cow_kills", 1)
		
def handle_cow_kill(player):
	if player.getAttribute("cow_kills") > 4:
		player.addAttribute("cow_kills", 0)
		player.sendMessage("You receive 10,000 coins for slaying 5 cows.")
		player.addCash(10000)
	else:
		player.addAttribute("cow_kills", player.getAttribute("cow_kills") + 1)