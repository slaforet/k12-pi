import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

#Create connection to minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Minecraft Whack-a-mole")

#get the position of the player
pos = mc.player.getTilePos()

#Create the gameboard
mc.setBlocks(pos.x-1, pos.y, pos.z+3,
             pos.x+1, pos.y+2, pos.z+3,
             block.STONE.id)

blocksLit = 0 #Number of blocks that are lit
points = 0 #Player score

time.sleep(5)
mc.postToChat("Get ready ...... RIGHT-CLICK to record points")
time.sleep(2)
mc.postToChat("GO!!")

while blocksLit < 9:
    for hitBlock in mc.events.pollBlockHits():
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
            mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.STONE.id)
            blocksLit= blocksLit - 1
            points = points +1
            
    time.sleep(0.4)
    blocksLit = blocksLit + 1
    lightCreated = False

    while not lightCreated:
        #Create a random positon on the gameboard
        xPos = pos.x + random.randint(-1,1)
        yPos = pos.y + random.randint(0,2)
        zPos = pos.z + 3

        #Check to see if the random position is a regular stone before changing its color
        if mc.getBlock(xPos, yPos, zPos) == block.STONE.id:
            mc.setBlock(xPos, yPos, zPos, block.GLOWSTONE_BLOCK.id)
            lightCreated = True

            
mc.postToChat("Game Over - Points: " +str(points))
