from com.pwnxile.core import Script
from com.pwnxile.core import Engine
from com.pwnxile.util import Misc
from com.pwnxile.rs2.player import PlayerHandler

gametime = 30
gamestarted = false
champion = "Nobody"
players = 0

def schedule():
	Engine.getTaskScheduler().schedule(Engine.getFightPits())
	print 'Minigame task has been scheduled for Fight Pits.'

def tick():	
	send_interface_update()
	if(!gamestarted)
		gametime--
	if(gametime == 0):
		startGame()
		gametime = 30;
	
def send_interface_update():
	for players in PlayerHandler.players:
		if(players != None):
			if (players.inFightPitsWait())
				send_wait_interface(players)
			elif (players.inFightPits())
				send_game_interface(players)

def send_wait_interface(p):
	p.getFunction().sendFrame126("Current Champion: JalYt-Ket-" + str(champion), 2805)
	p.getFunction().sendFrame126("Next game starting in : " + str(gameTime) + ".", 2806)
	p.getFunction().sendFrame36(560, 1)
	p.getFunction().walkableInterface(2804)
		
def send_game_interface(p):
	p.getFunction().sendFrame126("Current Champion: JalYt-Ket-" + str(champion), 2805)
	p.getFunction().sendFrame126("Foes remaining: " + str(playersInGame - 1), 2806)
	p.getFunction().sendFrame36(560, 1)
	p.getFunction().walkableInterface(2804)
			
def add_player(p):
	p.getFunction().walkableInterface(-1)
	p.getFunction().closeAllWindows()
	p.getFunction().movePlayer(2392 + Misc.random(12), 5139 + Misc.random(25), 0)
	players += 1

def remove_player(p):
	p.getFunction().movePlayer(2399, 5173, 0);
	if (players > 0)
		players -= 1
	if (players == 0):
		give_reward(p)
		end_game()
		
def give_reward(p):
	amount = (11 * p.combatLevel)
	p.getItems().addItem(6529, amount)
	p.addPxP(15);
	p.sendMessage("You receive " + str(amount) + " tokkul and 15 PxP for winning fight pits.")
	
	