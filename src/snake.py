from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create("minecraft-server")

mc.postToChat("snake...")
time.sleep(3)

x,y,z = mc.player.getPos()

current_position = [x,y,z]

while(True):
    current_position[random.randint(0,2)] += random.choice([-1,1])
    mc.setBlock(current_position[0], current_position[1], current_position[2], 12)
    time.sleep(0.1)


