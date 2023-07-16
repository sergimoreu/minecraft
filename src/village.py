from mcpi.minecraft import Minecraft
import time
from utils import House
import random

mc = Minecraft.create("minecraft-server")

mc.postToChat("village...")
time.sleep(5)
houses=[]
for u in range (0, 5):
    for o in range (0,5):
        h=House(mc,
        random.randint(3, 6),
        random.randint(5, 9), 
        random.randint(3, 6), 
        7*u,0,7*o,5, 17)
        houses.append (h)
for house in houses:
    house.spawn()
   
        