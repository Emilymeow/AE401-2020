from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

w = 10
h = 8
l = 20

mc.setBlocks(x,y,z,x+w,y+h,z+l,57)
mc.setBlocks(x+1,y+1,z+1, x+w-1,y+h-1,z+l-1, 57)
mc.player.setTilePos(x+2,y+2,z+2)