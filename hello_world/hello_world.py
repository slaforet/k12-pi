from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

pos = mc.player.getPos()
mc.postToChat("Hello everyone")
mc.postToChat("My position is: " + str(pos))

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 2)
