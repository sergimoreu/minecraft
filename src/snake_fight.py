from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create("minecraft-server")

mc.postToChat("snake...")
time.sleep(3)

x,y,z = mc.player.getPos()

current_position_water = [x,y,z]
current_position_lava = [x,y,z]


while(True):
    random_dir = [0] * 3
    random_dir[random.randint(0,2)] += random.choice([-1,1])
    for i in range(1, random.randint(1,20)):

        current_position_water[0] += random_dir[0]
        current_position_water[1] += random_dir[1]
        current_position_water[2] += random_dir[2]

        mc.setBlock(current_position_water[0] , current_position_water[1] , current_position_water[2], 11)
        time.sleep(0.01)

    
    random_dir = [0] * 3
    random_dir[random.randint(0,2)] += random.choice([-1,1])
    for i in range(1, random.randint(1,20)):

        current_position_lava[0] += random_dir[0]
        current_position_lava[1] += random_dir[1]
        current_position_lava[2] += random_dir[2]

        mc.setBlock(current_position_lava[0] , current_position_lava[1] , current_position_lava[2], 9)
        time.sleep(0.01)


