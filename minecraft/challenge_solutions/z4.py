#!/usr/bin/env python

import time
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

# while True: #dropping flowers
#     x,y,z = mc.player.getPos()
#     mc.setBlock(x,y,z,block.FLOWER_CYAN)
#     sleep(0.1)

while True: #either placing a gold block or dropping flowers 
    x,y,z = mc.player.getPos()
    if(mc.getBlock(x,y,z) == block.GOLD_BLOCK.id):
        mc.setBlock(x,y,z,block.FLOWER_YELLOW.id)
    else:
        mc.setBlock(x,y-1,z,block.GOLD_BLOCK.id)
    time.sleep(0.1)