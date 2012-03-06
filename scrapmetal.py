#author Ed
from org.pwnxile.core import Script

def dialogue_9101(player):
	player.npcMessage("Metal! Metal! Have to find metal!", 2024, "Strange Old Man")
   	player.nextChat = 9102

def dialogue_9102(player):
	player.playerMessage("Excuse me?")
   	player.nextChat = 9103

def dialogue_9103(player):
	player.npcMessage("What? Have you found the metal?", 2024, "Strange Old Man")
   	player.nextChat = 9104

def dialogue_9104(player):
	player.playerMessage("What's the problem, can I help?")
   	player.nextChat = 9105

def dialogue_9105(player):
	player.npcMessage("Will you help me collect some scrap metals?", 2024, "Strange Old Man")
   	player.nextChat = 9106

def dialogue_9106(player):
	player.playerMessage("What's in it for me?")
   	player.nextChat = 9107

def dialogue_9107(player):
	player.npcMessage("I suppose I could give you some money", 2024, "Strange Old Man")
   	player.nextChat = 9108

def dialogue_9108(player):
	player.npcMessage("How about 10 million gold coins?", 2024, "Strange Old Man")
   	player.nextChat = 9109

def dialogue_9109(player):
	player.playerMessage("Seems like a lot of effort for 10 million..")
   	player.nextChat = 9110

def dialogue_9110(player):
	player.npcMessage("Fine, how about 30 million, you can't refuse!", 2024, "Strange Old Man")
   	player.nextChat = 9111

def dialogue_9111(player):
	player.playerMessage("I suppose I could try and help you..")
   	player.nextChat = 9112

def dialogue_9112(player):
	player.npcMessage("Excellent young man!", "Scrap metal is scattered all around PwnXile", 2024, "Strange Old Man")
   	player.nextChat = 9113

def dialogue_9113(player):
	player.npcMessage("Could you go and collect 10 steel torches?", 2024, "Strange Old Man")
   	player.nextChat = 9114

def dialogue_9114(player):
	player.playerMessage("Where can I find these torches?")
   	player.nextChat = 9115

def dialogue_9115(player):
	player.npcMessage("That's for you to find out young man..", 2024, "Strange Old Man")
   	player.nextChat = 9116

def dialogue_9116(player):
	player.npcMessage("All I can say is that they will definately", "be under ground, so bring a spade!", 2024, "Strange Old Man")
   	player.nextChat = 9117

def dialogue_9117(player):
	player.playerMessage("I'll let you know when I have them.")
   	player.nextChat = 9118

def dialogue_9118(player):
	player.npcMessage("Thank you young chap.", 2024, "Strange Old Man")
   	player.nextChat = 0
	player.q2 = 1
	player.quest.sendQuests()
	
def dialogue_9119(player):
	player.npcMessage("Hurry up with that scrap metal!", 2024, "Strange Old Man")
   	player.nextChat = 0
