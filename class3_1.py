from mcpi.minecraft import Minecraft
mc=Minecraft.create()

count=0
while count<3:
    mc.postToChat('www')
    count=count+1