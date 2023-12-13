from math import ceil

from algorithms.iterative import checkNewSort
from resources.bin import Bin, binLoadSum, binIndex
from resources.binPrintToFile import binPrintToFile
from resources.item import Item
from resources.weightInform import WeightInform, itemWeight


def dotPWithMin_Bin(items, binSize, className, twist, min_bin):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    # r = open(f"results\{className}_Results_Steps.txt", "a")
    # if twist:
    #     if min_bin:
    #         r.write(f"\nDotP_Min_Bin-Twist{className}\n")
    #     else:
    #         r.write(f"\nDotP-Twist-{className}\n")
    # else:
    #     r.write(f"\nDotP_Min_Bin{className}\n")

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    allWeight = []  # [item] [bin] [weight]

    startSort = True

    SI1 = 0
    SI2 = 0
    SI3 = 0

    # Alsó korlát számítása
    for item in items:
        SI1 += item.d1
        SI2 += item.d2
        SI3 += item.d3

    LB1 = ceil(SI1 / binSize[1])
    LB2 = ceil(SI2 / binSize[1])
    LB3 = ceil(SI3 / binSize[1])

    LB = max(LB1, LB2, LB3)

    # r.write("A dotP majd az eredményen futtasuk a Min-Bin algoritmusokat a " + className + "osztályon!\n")

    # DotP algoritmus futtatása az inputon
    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
        # r.write(str(item) + "\n")

    while len(itemsCopy) > 0:
        for item in itemsCopy:
            for bin in bins:
                if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (bin.d3FreeCapacity >= item.getD3()):
                    item.itemWeight = int(item.d1) * int(bin.d1FreeCapacity) + int(item.d2) * int(bin.d2FreeCapacity) + int(item.d3) * int(bin.d3FreeCapacity)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
            # r.write(f"Új ládát kell nyitni! Láda szám: {len(bins)}\n")
            continue

        allWeight.sort(reverse=startSort, key=itemWeight)
        if twist:
            startSort = not startSort

        # for i in allWeight:
        #     r.write(str(i) + "\n")
        # r.write("\n")

        # r.write(f"Ezt a tárgyat teszük el: {allWeight[0].item}\n")
        bins[int(allWeight[0].bin.binIndex - 1)].addItem(allWeight[0].item)
        # r.write(f"Ebbe a ládába tettük a tárgyat: {bins[int(allWeight[0].bin.binIndex - 1)]}\n")
        # r.write("\n")

        itemsCopy.remove(allWeight[0].item)
        allWeight.clear()

    # r.write("A DotP futtatása utáni használt ládák: \n")

    # binPrintToFile(bins, r)

    # Futtasuk a Min-Bin algortimust a DotP eredményén

    UB = len(bins) # Felső korlát, az előző eredményből

    # r.write(f"Alsó korlát: {LB}, Felős korlát: {UB}\n")
    # r.close()

    if min_bin:
        isNewSort = True
        while isNewSort:
            bins, isNewSort = checkNewSortTest(bins, className)
        # r = open(f"results\{className}_Results_Steps.txt", "a")
        # r.write(f"Felhasznált ládák száma, a Min_Bin után: {len(bins)}\n")
        # r.close()

    a_r = open("results\All_Results.txt", "a")
    if twist:
        if min_bin:
            a_r.write(f"DotP_Min_Bin-Twist, {className}, {len(bins)}\n")
            a_r.close()
            return f"DotP_Min_Bin-Twist futattva lett a {className}-n!"
        else:
            a_r.write(f"DotP-Twist, {className}, {len(bins)}\n")
            a_r.close()
            return f"DotP-Twist futattva lett a {className}-n!"

    else:
        a_r.write(f"DotP_Min_Bin, {className}, {len(bins)}\n")
        a_r.close()
        return f"DotP_Min_Bin futattva lett a {className}-n!"


def checkNewSortTest(bins, className):
    # r = open(f"results\{className}_Results_Steps.txt", "a")

    bins.sort(reverse=False, key=binLoadSum)
    itemsCopy = []
    for b in range(len(bins)):
        leastLoadedBin = bins[b]

        # r.write("A legkevésbé tőltött láda: " + str(leastLoadedBin))

        for i in range(len(leastLoadedBin.getItems())):
            ldItem = leastLoadedBin.getItem(i)
            data = ldItem.split(" ")
            itemsCopy.append(Item(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
        # r.write(str(len(itemsCopy)) + "\n")

        bins.sort(reverse=True, key=binLoadSum)
        for bin in bins:
            if bin.binIndex == leastLoadedBin.binIndex:
                continue
            for item in itemsCopy:  # itt belenyúltam a kódba és még nem ellenőriztem le hupsz
                # r.write(str(item))
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