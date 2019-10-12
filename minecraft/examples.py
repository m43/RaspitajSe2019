########### 1 ###########
from mcpi import minecraft

mc = minecraft.Minecraft.create()
mc.postToChat("Hello world")
#########################


########### 2 ###########
import time
from mcpi import minecraft

mc = minecraft.Minecraft.create()

time.sleep(3)
position = pos.player.getPos()
mc.player.setPos(position.x, position.y, position.z+15)
#########################


########### 3 ###########
import time
from mcpi import minecraft

mc = minecraft.Minecraft.create()

while(True):
    time.sleep(6)
    x,y,z = mc.player.getPos()
    mc.player.setPos(x, y+30, z)
#########################


########### 4 ###########
import time
from mcpi import minecraft

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getPos()
mc.player.setPos(x,y+15,z)

mc.setBlock(x-1,y+10,z-1,1)
mc.setBlock(x-1,y+10,z,1)
mc.setBlock(x-1,y+10,z+1,1)
mc.setBlock(x,y+10,z-1,1)
mc.setBlock(x,y+10,z+1,1)
mc.setBlock(x+1,y+10,z-1,1)
mc.setBlock(x+1,y+10,z,1)
mc.setBlock(x+1,y+10,z+1,1)

# Other blocks you can try:
# 0 - air
# 1 - stone
# 2 - grass
# 3 - dirt
#########################


########### 5 ###########
import time
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getPos()
mc.player.setPos(x,y+15,z)

for i in [-1,0,1]:
    for j in [-1,0,1]:
        mc.setBlock(x+i,y+10,z+j, block.STONE.id)
#########################


########### 6 ###########
import time
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getPos()

time.sleep(6)
for i in range(-100, 101, 1):
    for j in range(-100,101,1):
        mc.setBlock(x+i,y+12,z+j, block.SAND.id)
#########################


# Task: participants should go through "introduction.py" by themselves


########### 7 ###########
import time
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getPos()

time.sleep(3)

mc.setBlock(x-1,y+1,z-1, block.TNT.id)
mc.setBlock(x-6,y+2,z-6, block.TNT.id, 1)

mc.setBlocks(x+1,y+1,z+1,x+12,y+12,z+12, block.TNT.id, 1)
#########################


########### 8 ###########
import time
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
x,y,z = mc.player.getPos()
time.sleep(3)

mc.setBlocks(x+10,y,z+10,x-10,y-10,z-10,block.AIR.id)
mc.setBlocks(x+10,y+3,z+10,x+10+3,y+3+3,z+10+3,block.DIAMOND_BLOCK.id)
mc.setBlocks(x+10+1,y+3+1,z+10+1,x+10+3+1,y+3+3+1,z+10+3+1,block.OBSIDIAN.id)
#########################


# TASK 1: challenge1.png -- create an empty room with an opening of some kind, just like on the pic

# TASK 2: challenge2.png - create a sphere
for x in range(radius*-1,radius):
	for y in range(radius*-1, radius):
		for z in range(radius*-1,radius):
			if x**2 + y**2 + z**2 < radius**2:
				mc.setBlock(playerPos.x + x, playerPos.y + y + radius, playerPos.z - z - 10, block.GOLD_BLOCK)



# TASK 3: challenge3.png - filled circles
for i in range(-radius, radius+1, 1):
    for j in range(-radius, radius+1, 1):
        if(i*i+j*j < radius):
            mc.setBlock(x+i,y+j,z, block.WOOL.id, color)



# TASK 4: challenge4.png - creating bridges as you walk ...or dropping blocks as you walk (for example flowers)
while True: #dropping flowers
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,block.FLOWER_CYAN)
    sleep(0.1)
while True: #either placing a gold block or dropping flowers 
    x,y,z = mc.player.getPos()
    if(mc.getBlock(x,y,z) == block.GOLD_BLOCK.id):
        mc.setBlock(x,y,z,block.FLOWER_YELLOW.id)
    else:
        mc.setBlock(x,y-1,z,block.GOLD_BLOCK.id)
    sleep(0.1)


########### 10 ###########
#!/usr/bin/env python
from mcpi import minecraft
from mcpi import block

if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    x,y,z = mc.player.getPos()
    
    mc.setBlock(x+3,y+3,z, block.LAVA_FLOWING.id)
    sleep(12)

    mc.setBlock(x+3,y+3,z, block.WATER_FLOWING.id)
    sleep(6)
    mc.setBlock(x+3,y+5,z, block.AIR.id)
##########################


# TASK 5: add waterfall above the sphere from previous task

#########################################################################
### The following examples (located in ./examples) are added as well. ### 
### They were just collected on the internet. If interested in the    ###
### way the program works and creates a rainbow for example, one can  ###
### examine the written code further.                                 ###
### (My favourites are: rainbow, digital clock and snake)             ###
#########################################################################
# examples: rainbow
# examples: magic
# examples: bunkermagic
# examples: drawbuilding
# examples: maze
# examples: hideandseek
# examples: tntsnake
# examples: draw mandelbrot


# Special challenges:
#   --> [3D] create a Sierpinski cube 
#   --> [2D] create a Sierpinski carpet
# for help use google and perhaps this resource: www.fractal-explorer.com/minecraftsponge.html


# examples --> snake
# examples --> digital clock
# examples --> analog clock
# examples --> digital clock 2
# examples --> minesweeper