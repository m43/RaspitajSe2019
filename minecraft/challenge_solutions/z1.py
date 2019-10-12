#!/usr/bin/env python

import time
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
x,y,z = mc.player.getPos()
# time.sleep(3)

#house start
hx = x + 3
hy = y - 1
hz = z + 3
hsize = 6
hwalls = 1
hdoor = 2

mc.setBlocks(hx,hy,hz,
        hx+hsize, hy+hsize, hz+hsize,
        block.OBSIDIAN.id)
mc.setBlocks(hx+hwalls,hy+hwalls,hz+hwalls,
        hx+hsize-hwalls, hy+hsize-hwalls, hz+hsize-hwalls,
        block.AIR.id)
mc.setBlocks(hx+1,hy+1,hz,
        hx+1+hdoor, hy+1+hdoor, hz,
        block.AIR.id)