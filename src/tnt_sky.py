from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create("minecraft-server")

mc.postToChat("tnt sky...")
time.sleep(3)

x,y,z = mc.player.getPos()

# tnt
for i in range(0, 50):
    for j in range (0, 50):
        mc.setBlock(x+i, y -3 , z+j, 46,1)

# pedra
for i in range(0, 50):
    for j in range (0, 50):
        mc.setBlock(x+i, y -4 , z+j, 1,1)

# foc
for i in range(0, 50):
    for j in range (0, 50):
        mc.setBlock(x+i, y -2 , z+j, 51,1)

# tnt
for i in range(0, 50):
    for j in range (0, 50):
        mc.setBlock(x+i, y -1 , z+j, 46,1)
