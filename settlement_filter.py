import time
import math
import random
import numpy as np
import pymclevel as pmcl
#  from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
import mcplatform
#  from mcplatform import *
import utilityFunctions as utilityFunctions

from pprint import pprint

inputs = (
         ("Mank's test", "label"),
         ("Material", pmcl.alphaMaterials.Cobblestone),
         ("Creator: Josh Mankelow", "label"),
         )


class Helper:
    # Likely to be very inefficient if used across a big box.
    # TODO Optimise
    def generate_terrain_heightmap(self, level, box):
        range_x = box.maxx - box.minx
        range_y = box.maxy - box.miny
        range_z = box.maxz - box.minz
        heightmap = np.zeros((range_x, range_z))
        for x in range(range_x):
            adj_x = x + box.minx
            for z in range(range_z):
                adj_z = box.minz + z
                for y in range(range_y, 0, -1):
                    adj_y = box.miny + y
                    current_block = level.blockAt(adj_x, adj_y, adj_z)
                    if current_block != 0:
                        break
                    #  while current_block is not pmcl.alphaMaterials.air.ID:

                heightmap[x, z] = adj_y

        return heightmap


# 0: Parameters
# 1: the level (the minecraft world).
# 2: the selected box from mcedit.
# 3: User defined inputs from mcedit
def perform(level, box, options):
    helper = Helper()
    print("Performing!")

    #  block = level.blockAt(box.minx, box.miny, box.minz)
    #  print(block)
    #  print(pmcl.alphaMaterials.Cobblestone.ID)
    heightmap = helper.generate_terrain_heightmap(level, box)
    pprint(heightmap)

    print("Ending perform!")
