from mcpi.minecraft import Minecraft
mc = Minecraft.create()

px,py,pz = mc.player.getTilePos()

def plantTree(x,y,z):
    mc.setBlocks(x-2,y+4,z-2, x+2,y+8,z+2, 18)
    mc.setBlocks(x,y,z, x,y+5,z, 17)

for i in range(10):
    plantTree(px+i*20,py,pz+i*20)