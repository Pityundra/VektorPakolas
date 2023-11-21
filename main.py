from resources.bin import Bin
from resources.item import Item
from resources.simpleLowerBound import SimpleLowerBound
from algorithms.dotPWithMin_Bin import dotPWithMin_Bin
from algorithms.ffd import FFD
from algorithms.geometricHeuristics import GH
from resources.dataLoad import fileRead
from algorithms.iterative import min_bin
from algorithms.test import FFDRev, FFDVal, FFDGroups, FFDRatio, FFDBox, L2NotDet, FFDRevAdv
from badExamples.py import badExamplesWithOneBigDimension
from badExample.py import badExample

badExample()


def runAlgorithms():
    f = open("data\FileNames.txt", "r")
    lines = f.readlines()

    items2 = []
    binSize2 = []
    for line in lines:
        line = line.strip()
        items, binSize = fileRead(line)
        # print(binSize)
        # print(line)
        line = line.lstrip("data\\")
        line = line.lstrip("dataOpt\\")
        print(line)

        # print(GH(items, "L2", binSize, 1, line))
        # print(GH(items, "L2", binSize, 5, line))
        # print(GH(items, "dotP", binSize, 1, line))
        # print(GH(items, "dotP", binSize, 5, line))
        # print(FFD(items, "item", "sum", binSize, line))
        # print(FFD(items, "item", "avg", binSize, line))
        # print(FFD(items, "item", "prod", binSize, line))
        # print(FFD(items, "bin", "sum", binSize, line))
        # print(FFD(items, "bin", "avg", binSize, line))
        # print(FFD(items, "bin", "prod", binSize, line))
        # print(min_bin(items, binSize, line))
        # print(dotPWithMin_Bin(items, binSize, line, True, False))
        # print(dotPWithMin_Bin(items, binSize, line, True, True))
        # print(dotPWithMin_Bin(items, binSize, line, False, True))

        print("Alsó korlát: " + str(SimpleLowerBound(items, binSize, line)))

        notDetAlgsCall(FFDBox, 100, items, binSize)
        notDetAlgsCall(FFDGroups, 100, items, binSize)

        items.clear()
        binSize.clear()


def notDetAlgsCall(algName, runTime, items, binSize):
    name = str(algName).strip().split()
    print(f"{name[1]}: ", end="")
    res = []
    for i in range(runTime):
        res.append(algName(items, binSize))
    print(res)
    print({i: res.count(i) for i in res})
    print("Átlag:" + str(sum(res)/len(res)))
    print()


# dataGen()
# generateClasses()
# runAlgorithms()
badExamplesWithOneBigDimension("test", 1000, 10)

# items, binSize = fileRead("data\class1_200.txt")
#
# for i in range(10):
#     print(FFDRev(items, binSize))


# L2NotDet(items, binSize)
# SimpleLowerBound(items, binSize, "class1_25")

# dataClass2("Spinned", 100, 10)

# print("FFDRev: " + str(FFDRev(items, binSize)))
# print("FFDRevAdv: " + str(FFDRevAdv(items, binSize)))
# print("FFDVal: " + str(FFDVal(items, binSize)))
# print("FFDRatio: " + str(FFDRatio(items, binSize)))
# print("FFDGroups: " + str(FFDGroups(items, binSize)))
# print("FFDBox: " + str(FFDBox(items, binSize)))
# print()
# print("L2NotDet: " + str(L2NotDet(items, binSize)) + "\n")