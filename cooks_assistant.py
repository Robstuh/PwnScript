#Cook's Assistant is the first RuneScape quest ever released
#PwnScript conversion by Robbie

from com.pwnxile.core import Script
from com.pwnxile.rs2.plugin import DialogueSequence

cook = 278 #NPC ID
part_one = DialogueSequence(1)
part_two = DialogueSequence(2)
part_three = DialogueSequence(3)

def sequence_1():
	part_one.playerSay("What's wrong?")
	part_one.npcSay(cook, "Oh dear, oh dear oh dear, I'm in a terrible terrible", "mess! It's the Duke's birthday today, and I should be", "making him a lovely, big birthday cake using special", "ingredients...")
	part_one.npcSay(cook, "...but I've forgotten to get the ingredients. I'll never get", "them in time now. He'll sack me! What ever will i do? I", "have four children and a goat to look after. Would you", "help me? Please?")
	part_one.playerSay("I'm always happy to help a cook in distress.")
	part_one.npcSay(cook, "Thank Saradomin! ")
	
def sequence_2():
	part_two.npcSay(cook, "How are you getting on with finding the ingredients?")
	part_two.playerSay("I haven't got any of them yet, I'm still looking.")
	part_two.npcSay(cook, "Please get the ingredients quickly. I'm running out of", "time! The Duke will throw me onto the street!", "You still need to get:", "Some flour. some milk. An egg.")
	part_two.playerSay("Where can I find the ingredients?")
	part_two.npcSay(cook, "That's the problem: i don't exactly know. I usually",
"send my assistant to get them for me but he quit.")

def sequence_3():
	part_three.playerSay("Here you go")
	part_three.npcSay(cook, "You've given me everything I need! I am saved!", "Thank you!")
	part_three.playerSay("So do I get to go to the Duke's party?")
	part_three.npcSay(cook, "I'm afraid not. Only the big cheeses get to Dine with the Duke.")
	part_three.playerSay("Well maybe one day I'll be important enough to sit at the Duke's table.")
	part_three.npcSay(cook, "Maybe, but I won't be holding my breath.")
	