from math import ceil
from bin import Bin, binLoadSum, binIndex
from item import itemsSum, itemsAVG, Item


# dataClass("class1", 1000, 1000, 1000, i, 100, 400, 100, 400, 100, 400)


def min_bin(items, binSize):
    binsIndex = 0
    bins = []
    SI1 = 0
    SI2 = 0
    SI3 = 0

    for item in items:
        SI1 += item.d1
        SI2 += item.d2
        SI3 += item.d3

        bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
        bins[binsIndex].addItem(item)
        binsIndex += 1

    LB1 = ceil(SI1 / binSize[1])
    LB2 = ceil(SI2 / binSize[1])
    LB3 = ceil(SI3 / binSize[1])

    LB = max(LB1, LB2, LB3)
    UB = len(
        items)  # a DotProduct értékét vettéka cikben, jelenleg nem látom értelmét, mert nem lenne túl sok opció amit megvizsgálnánk

    print(f"Alsó korlát: {LB}")
    print(f"Felős korlát: {UB}")

    m = range(LB, UB)
    for bin in bins:
        print(bin)
    print("\n")

    isNewSort = True
    while isNewSort:
        bins, isNewSort = checkNewSort(bins)
        for bin in bins:
            print(bin)
        print("\n")


def checkNewSort(bins):

    bins.sort(reverse=False, key=binLoadSum)
    itemsCopy = []
    leastLoadedBin = bins[0]
    print(leastLoadedBin)
    for i in range(len(leastLoadedBin.getItems())):
        ldItem = leastLoadedBin.getItem(i)
        data = ldItem.split(" ")
        itemsCopy.append(Item(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
    print(len(itemsCopy))

    bins.sort(reverse=True, key=binLoadSum)
    for bin in bins:
        if bin.binIndex == leastLoadedBin.binIndex:
            continue
        for i in range(len(leastLoadedBin.getItems())):
            if (bin.d1FreeCapacity >= itemsCopy[i].getD1()) and (bin.d2FreeCapacity >= itemsCopy[i].getD2()) and (
                    bin.d3FreeCapacity >= itemsCopy[i].getD3()):
                bin.addItem(itemsCopy[i])
                print(itemsCopy[i])
                print("\n")
                itemsCopy.remove(itemsCopy[i])
        if not itemsCopy:
            bins.sort(key=binIndex)
            bins.remove(leastLoadedBin)
            return bins, True
    return bins, False
