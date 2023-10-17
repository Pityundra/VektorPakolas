from algorithms.dotPWithMin_Bin import dotPWithMin_Bin
from algorithms.ffd import FFD
from algorithms.geometricHeuristics import GH
from resources.dataLoad import fileRead
from algorithms.iterative import min_bin
from resources.bin import Bin
from resources.item import Item

# GH(items, L2/dotP, binSize, grasp, className)
# FFD(items, bin/item, sum/avg, binSize, className)

# dataGen()
# generateClasses()

f = open("data\FileNames.txt", "r")
lines = f.readlines()

for line in lines:
    line = line.strip()
    items, binSize = fileRead(line)
    # print(binSize)
    line = line.lstrip("data\\")
    line = line.lstrip("dataWithOpt\\")
    print(GH(items, "L2", binSize, 1, line))
    print(GH(items, "L2", binSize, 5, line))
    print(GH(items, "dotP", binSize, 1, line))
    print(GH(items, "dotP", binSize, 5, line))
    print(FFD(items, "item", "sum", binSize, line))
    print(FFD(items, "item", "avg", binSize, line))
    print(FFD(items, "item", "prod", binSize, line))
    print(FFD(items, "bin", "sum", binSize, line))
    print(FFD(items, "bin", "avg", binSize, line))
    print(FFD(items, "bin", "prod", binSize, line))
    print(min_bin(items, binSize, line))
    print(dotPWithMin_Bin(items, binSize, line, True, False))
    print(dotPWithMin_Bin(items, binSize, line, True, True))
    print(dotPWithMin_Bin(items, binSize, line, False, True))
    items.clear()
    binSize.clear()

"""

items, binSize = fileRead("data\class1_200.txt")
dotPWithMin_Bin(items, binSize, "class1_25.txt", True, False)
"""