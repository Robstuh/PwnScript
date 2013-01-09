from com.pwnxile.util import Misc
from com.pwnxile.world.objects import CustomObjects

def command_wat(player):
	player.getFunction().clippedStep()
	
def click_item_299(player):
	player.deleteItem(299, 1)
	x = player.getX()
	y = player.getY()
	player.addAttribute("flower_random", Misc.random(8))
	player.getFunction().object(2980 + player.getAttribute("flower_random"), x, y, 0, 10)
	player.getFunction().clippedStep()
	player.turnPlayerTo(x, y)
	player.addAttribute("flower_x", x)
	player.addAttribute("flower_y", y)
	player.dialogueOption("Pick the flowers", 2440, "Leave the flowers", 2442)
	
def chat_2440(player): # pick flowers
	if player.hasAttribute("flower_x"):
		player.startAnimation(827)
		player.getFunction().closeAllWindows()
		player.getFunction().object(-1, player.getAttribute("flower_x"), player.getAttribute("flower_y"), 0, 10)
		player.addItem(2460 + (player.getAttribute("flower_random") * 2))

def chat_2442(player):	# leave flowers	
	if player.hasAttribute("flower_x"):
		World.addObject(2980 + player.getAttribute("flower_random"), player.getAttribute("flower_x"), player.getAttribute("flower_y"))
		player.sendMessage("You leave the flowers, how pretty!")
		player.getFunction().closeAllWindows()