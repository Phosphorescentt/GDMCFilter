import time
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

import utilityFunctions as utilityFunctions

inputs = (
	("Mank's test", "label"),
	("Material", alphaMaterials.Cobblestone),
        ("Creator: Josh Mankelow", "label"),
	)


# 0: Parameters
# 1: the level (aka the minecraft world).
# 2: the selected box from mcedit.
# 3: User defined inputs from mcedit
def perform(level, box, options):
    print("Performing!")

    for x in range(box.minx, box.maxx):
        for y in range(box.miny, box.maxy):
            for z in range(box.minz, box.maxz):
                utilityFunctions.setBlock(level, (options["Material"].ID, 0), x, y, z)

    print("Ending perform!")
