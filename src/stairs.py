from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create("minecraft-server")

mc.postToChat("Stairs")

x,y,z = mc.player.getPos()

for i in range(0, 20):
    mc.setBlock(-i  - 4, y + i, z+i, 1)