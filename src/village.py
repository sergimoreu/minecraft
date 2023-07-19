from mcpi.minecraft import Minecraft
import time
from utils import House, Tree, RandomForest
import random

mc = Minecraft.create("minecraft-server")

mc.postToChat("house...")

h=House(mc,
        4,
        5, 
        6, 
        0,0,0, 17, 20)

h.spawn()

# time.sleep(2)
# houses=[]
# for u in range (0, 5):
#     for o in range (0,5):
#         h=House(mc,
#         random.randint(3, 6),
#         random.randint(5, 9), 
#         random.randint(3, 6), 
#         7*u,0,7*o,5, 17)
#         houses.append (h)
# for house in houses:
#     house.spawn()
   

# TREE
# player_x, player_y, player_z = mc.player.getPos()

# pos_x = 0
# pos_y = 0
# pos_z = 0
# trunk_height = 100
# leaves_size = 50
# trunk_material = 17
# leaves_material = 46 

# t=Tree(mc, player_x, player_y, player_z, pos_x, pos_y, pos_z, trunk_height, leaves_size, trunk_material, leaves_material)
# t.spawn_square()     


# RANDOM FOREST

# player_x, player_y, player_z = mc.player.getPos()

# random_forest = RandomForest(
#     mc,
#     player_x, player_y, player_z,
#     0,
#     0,
#     0,
#     20,
#     17,
#     17,
# )
# mc.postToChat(f"Spawning random forest at {player_x} {player_y} {player_z}")

# random_forest.spawn()