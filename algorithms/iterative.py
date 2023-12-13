from math import ceil
from resources.bin import Bin, binLoadSum, binIndex
from resources.binPrintToFile import binPrintToFile
from resources.item import Item


def min_bin(items, binSize, className):
    # r = open(f"results\{className}_Results_Steps.txt", "a")
    # r.write(f"\nmin_bin-{className}\n")

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
    UB = len(items)
    # a DotProduct értékét vettéka cikben, jelenleg nem látom értelmét, mert nem lenne túl sok opció amit megvizsgálnánk

    # r.write(f"Alsó korlát: {LB}, Felős korlát: {UB}\n")

    # m = range(LB, UB)

    # binPrintToFile(bins, r)
    # r.close()

    isNewSort = True
    while isNewSort:
        bins, isNewSort = checkNewSort(bins, className)

    # r = open(f"results\{className}_Results_Steps.txt", "a")
    # r.write(f"Felhasznált ládák száma: {len(bins)}\n")
    # r.close()

    a_r = open("results\All_Results.txt", "a")
    a_r.write(f"min_bin, {className}, {len(bins)}\n")
    a_r.close()

    return f"min_bin futattva lett a {className}-n!"


def checkNewSort(bins, className):

    # r = open(f"results\{className}_Results_Steps.txt", "a")

    bins.sort(reverse=False, key=binLoadSum)
    itemsCopy = []
    leastLoadedBin = bins[0]
    # r.write("A legkevésbé tőltött láda: " + str(leastLoadedBin))

    for i in range(len(leastLoadedBin.getItems())):
        ldItem = leastLoadedBin.getItem(i)
        data = ldItem.split(" ")
        itemsCopy.append(Item(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
    # print(str(len(itemsCopy)) + "\n")

    bins.sort(reverse=True, key=binLoadSum)
    for bin in bins:
        if bin.binIndex == leastLoadedBin.binIndex:
            continue
        for item in itemsCopy:  # itt belenyúltam a kódba és még nem ellenőriztem le hupsz
            if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (
                    bin.d3FreeCapacity >= item.getD3()):
                bin.addItem(item)
                # r.write(str(item) + "\n")
                # r.write("A " + str(item.getNumber()) + " számú tárgyat át raktuk a " + str(leastLoadedBin.binIndex) + " ládából a " + str(bin.getBinIndex()) + " ládába!\n")
                itemsCopy.remove(item)
        if not itemsCopy:
            bins.remove(leastLoadedBin)
            bins.sort(key=binIndex)
            # binPrintToFile(bins, r)
            # r.close()
            return bins, True
    # binPrintToFile(bins, r)
    # r.close()
    return bins, False


