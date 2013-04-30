#==============================================================================
#title           : Donor content script
#description     : A script to handle donor related game content
#author          : Unknown
#date            : 24/1/2013
#version         : 1.3
#notes           : Finished
#==============================================================================

from com.pwnxile.core import World
from com.pwnxile.rs2 import Position
from com.pwnxile.rs2 import Location
from com.pwnxile import GameConfig

donor_island = Location.DONOR_ISLAND

def first_click_npc_554(player):
	if player.isDonator():
		player.dialogueOption("Who are you?", 2649, "How many donor points do I have?", 2660)
	else:
		player.dialogueOption("Who are you?", 2649, "Ask about Donator status", 2655, "How many donor points do I have?", 2660)

def second_click_npc_554(player):
	player.getShop().openShop(40)

def first_click_object_2156(player):
	if player.isDonator():
		player.teleport(Position.DONOR_ISLAND_SPAWN)
	else:
		player.boxMessage("You must be a donator to use this portal.")
		
def is_on_island(player):
	if donor_island.isInLocation(player):
		return True
	return False
	
def chat_2649(p):
	p.playerChat("Who are you?")
	p.nextChat(2651)
	
def chat_2650(p):
	p.playerChat("Who are you again?")
	p.nextChat(2651)

def chat_2651(p):
	p.npcChat("Hi, I'm a shopkeeper.", "It's my job to exchange donor points in", "return for various donation items.")
	p.nextChat(2652)
	
def chat_2652(p):
	p.playerChat("Could I sell what you have to sell?")
	p.nextChat(2653)
	
def chat_2653(p):
	p.npcChat("Yes of course.", "You'll need to donate for points however", "if you wish to purchase an item from me.")
	p.nextChat(2654)
	
def chat_2654(p):
	p.getShop().openShop(40)
	
def chat_2655(p):
	p.playerChat("How do I receive donator status?")
	p.nextChat(2656)

def chat_2656(p):
	p.npcChat("You can purchase it from me.", "I will grant you donator status in return", "for 20 donator points.")
	p.nextChat(2657)
	
def chat_2657(p):
	p.dialogueOption("Buy donator status", 2658, "Cancel", 0)
	
def chat_2658(p):
	p.endChat()
	if p.donorPoints > 20:
		p.donorPoints -= 20
		GameConfig.donators.add(p.playerName2)
		p.boxMessage("You are now a donator.")
	else:
		p.boxMessage("You need 20 donator points to purchase status.")
		
def chat_2660(p):
	p.npcChat("You have " + str(p.donorPoints) + " donator points.")
	p.endChat()
