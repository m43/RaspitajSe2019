#!/usr/bin/env python

from mcpi import minecraft
from mcpi import block
from math import *

mc = minecraft.Minecraft.create()

def filled_circle(mc, x, y, z, color, radius):
        for i in range(-radius, radius+1, 1):
                for j in range(-radius, radius+1, 1):
                        if(i*i+j*j < radius):
                                mc.setBlock(x+i,y+j,z, block.WOOL.id, color)

#colors

yellow=4
green=5

x,y,z = mc.player.getPos()

filled_circle(mc, x,y,z+10, green, 100)
filled_circle(mc, x,y,z+10, yellow, 60)
