from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create("minecraft-server")

mc.postToChat("random carpet...")
time.sleep(3)

x,y,z = mc.player.getPos()

# random
for i in range(0, 50):
    for j in range (0, 50):
        # r= #random.randint(0,98)
        mc.setBlock(x+i, y -3 , z+j, i+j)
        # mc.postToChat(r)
        time.sleep(0.0005)

