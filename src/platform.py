from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create("minecraft-server")

mc.postToChat("platform...")
time.sleep(3)

x,y,z = mc.player.getPos()

for i in range(0, 50):
    for j in range (0, 50):
        for l in range (0, 50):
            mc.setBlock(x+i, y+l , z+j, 2)
            time.sleep(0.0005)

