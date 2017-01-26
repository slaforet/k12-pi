from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

"""
WOOD_PLANKS
WATER_STATIONARY
GOLD_ORE
GOLD_BLOCK block.GOLD_BLOCK.id
DIAMOND_BLOCK
NETHER_REACTOR_CORE
"""
#mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, block.GOLD_BLOCK.id)

"""flower = 38
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock (x, y, z, flower)
    sleep(0.1)
"""

"""while True:
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y-1, z)
    print (block_beneath)

"""

lava = 10
water = 8
air = 0

x, y, z = mc.player.getPos()


mc.setBlock(x+3, y+3, z, lava)
sleep(20)
mc.setBlock(x+3, y+5, z, water)
sleep(4)
mc.setBlock(x+3, y+5, z, air)

