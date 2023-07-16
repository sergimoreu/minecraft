from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create("minecraft-server")

mc.postToChat("Column")

time.sleep(4)

x,y,z = mc.player.getPos()

for i in range(0, 100):
    for j in range(0, 100):
        time.sleep(0.0005)
        mc.setBlock(x + (i//10) * 5, y + i%10, z + (j//10) * 5, 46, 1)