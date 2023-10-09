from bin import Bin
from dataLoad import fileRead
from geometricHeuristics import GH
from ffd import FFD
from item import Item, itemsSum, itemsAVG
from dataGenerate import generateClasses
from dataGenerate2 import dataGen
from iterative import min_bin

# GH(items, L2/dotP, binSize, grasp, className)
# FFD(items, bin/item, sum/avg, binSize, className)

# dataGen()
# generateClasses()

f = open("data2\FileNames.txt", "r")
lines = f.readlines()

for line in lines:
    line = line.strip()
    items, binSize = fileRead(line)
    # print(binSize)
    line = line.lstrip("data\\")
    line = line.lstrip("data2\\")
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
    items.clear()
    binSize.clear()

"""

items, binSize = fileRead("data\class1_25.txt")
# print(FFD(items, "bin", "avg", binSize, "class6_5.txt"))
min_bin(items, binSize)


"""