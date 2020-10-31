from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

count=0
while count<100:
    mc.setBlock(x, y + count, z, 57)

    count=count + 1
    