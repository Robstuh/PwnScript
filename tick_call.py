#Tick script by Robbie
from org.pwnxile.core import Script

def world_tick(engine):
	engine.getItemHandler().tick()
	engine.getShopHandler().tick()
	engine.getObjectHandler().tick()
	engine.getObjectManager().tick()
	
def entity_updating(engine):	
	engine.getNpcHandler().tick()
	engine.getPlayerHandler().tick()

def game_tick(engine):
	engine.getCastleWars().tick()
	engine.getPestContol().tick()
	engine.getFightPits().tick()
	