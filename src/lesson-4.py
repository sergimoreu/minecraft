from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create("minecraft-server")



x,y,z = mc.player.getPos()
mc.postToChat(z)


for q in range(100):
    for i in range(20):
        mc.setBlock(x + q,y + i,z,46)
        time.sleep(0.2)