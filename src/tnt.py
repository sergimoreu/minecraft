from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create("minecraft-server")

mc.postToChat("TNT!!!")

# x,y,z = mc.player.getPos()
# mc.player.setPos(x,y+20,z)
x,y,z = mc.player.getPos()

mc.setBlocks(
    x - 20 , y , z,
    x -20 + 5, y + 5, z + 5,
    block.TNT.id,
    1
    )
