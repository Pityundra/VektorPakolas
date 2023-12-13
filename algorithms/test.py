import numpy as np

from math import ceil
from resources.bin import Bin
from resources.binPrintToFile import binPrintToFile
from resources.item import itemsSum, itemsAVG, itemsProd
from resources.weightInform import WeightInform, itemWeight


def FFDRev(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    items.sort(reverse=True, key=itemsSum)
    rev = False

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    # for item in itemsCopy:
    #     print(str(item) + '\n')
    # print('\n')

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    for i in range(len(itemsCopy)):
        # print(i)
        item = itemsCopy[0]
        # print(item)
        bin, binsIndex = placeItem(item, bins, binsIndex, binSize)
        itemsCopy.remove(item)
        itemsCopy.sort(reverse=rev, key=itemsSum)
        rev = not rev


    # for bin in bins:
    #     print(str(bin) + "\n")
    # print("\n")
    #
    # print(f"Felhasznált ládák száma: {len(bins)}\n")

    return len(bins)


def FFDRevForBadExample(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    items.sort(reverse=True, key=itemsSum)

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    while len(itemsCopy):
        # print(i)
        itemF = itemsCopy[0]
        itemL = itemsCopy[len(itemsCopy)-1]
        # print(itemF)
        # print(itemL)
        bin, binsIndex = placeItem(itemF, bins, binsIndex, binSize)
        bin, binsIndex = placeItem(itemL, bins, binsIndex, binSize)
        itemsCopy.remove(itemF)
        itemsCopy.remove(itemL)

    # for bin in bins:
    #     print(str(bin) + "\n")
    # print("\n")
    #
    # print(f"Felhasznált ládák száma: {len(bins)}\n")

    return len(bins)


def FFDRevAdv(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    items.sort(reverse=True, key=itemsSum)
    rev = False

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    while len(itemsCopy):
        # print(i)
        item = itemsCopy[0]
        bin, binsIndex = placeItem(item, bins, binsIndex, binSize)
        # print("nagy")
        itemsCopy.remove(item)

        # for bin in bins:
        #     print(str(bin) + "\n")
        # print("\n")

        for bin in bins:
            if len(itemsCopy) > 0 and (bin.d1FreeCapacity >= itemsCopy[len(itemsCopy)-1].getD1()) and (bin.d2FreeCapacity >= itemsCopy[len(itemsCopy)-1].getD2()) and (
                    bin.d3FreeCapacity >= itemsCopy[len(itemsCopy)-1].getD3()):
                bin.addItem(itemsCopy[len(itemsCopy)-1])
                # print("kicsi")
                itemsCopy.remove(itemsCopy[len(itemsCopy)-1])

                while len(itemsCopy):
                    # print(i)
                    item = itemsCopy[0]
                    bin, binsIndex = placeItem(item, bins, binsIndex, binSize)
                    # print("vált")
                    itemsCopy.remove(item)
                    itemsCopy.sort(reverse=rev, key=itemsSum)
                    rev = not rev

    # for bin in bins:
    #     print(str(bin) + "\n")
    # print("\n")
    #
    # print(f"Felhasznált ládák száma: {len(bins)}\n")

    return len(bins)


def FFDVal(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    items.sort(reverse=True, key=itemsSum)

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    # for item in itemsCopy:
    #     print(str(item) + '\n')
    # print('\n')

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    for i in range(len(itemsCopy)):
        # print(i)
        # for item in itemsCopy:
        #     print(str(item) + '\n')
        # print('\n')

        number = np.random.random_integers(1, 4)
        if number == 4:
            item = itemsCopy[len(itemsCopy) - 1]
            # print("vége " + str(len(itemsCopy)))
        elif number == 3:
            # print("közepe " + str(ceil((len(itemsCopy)) / 2)))
            item = itemsCopy[round((len(itemsCopy))/2)-1]
        else:
            item = itemsCopy[0]
            # print("eleje")

       # print(str(item))

        bin, binsIndex = placeItem(item, bins, binsIndex, binSize)
        itemsCopy.remove(item)

    # for bin in bins:
    #     print(str(bin) + "\n")
    # print("\n")
    #
    # print(f"Felhasznált ládák száma: {len(bins)}\n")

    return len(bins)


def FFDRatio(items, binSize):
    # 1/4 eséllyel a végéről rakunk el egy tárgyat
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    items.sort(reverse=True, key=itemsSum)

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    # for item in itemsCopy:
    #     print(str(item) + '\n')
    # print('\n')

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    for i in range(len(itemsCopy)):
        number = np.random.random_integers(1, 4)
        if number == 4:
            item = itemsCopy[len(itemsCopy) - 1]
            # print("vége " + str(len(itemsCopy)))
        else:
            item = itemsCopy[0]
            # print("eleje")

        bin, binsIndex = placeItem(item, bins, binsIndex, binSize)
        itemsCopy.remove(item)

    # for bin in bins:
    #     print(str(bin) + "\n")
    # print("\n")

    # print(f"Felhasznált ládák száma: {len(bins)}\n")

    return len(bins)


def FFDGroups(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    groupNumber = 3

    items.sort(reverse=True, key=itemsSum)

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
    #     print(str(item) + '\n')
    # print('\n')

    splitNumber = int(ceil(len(itemsCopy) / groupNumber))
    # print(splitNumber)

    for j in range(groupNumber):
        if j == groupNumber-1:
            for i in range(len(itemsCopy)):
                random = np.random.random_integers(0, len(itemsCopy)-1)
                bins, binsIndex = placeItem(itemsCopy[random], bins, binsIndex, binSize)
                itemsCopy.remove(itemsCopy[random])
            # print(f"Elraktuk az összes tárgyat! ItemsCopy lista hossza: {len(itemsCopy)}\n")
        else:
            for i in range(splitNumber-1):
                random = np.random.random_integers(0, splitNumber-1-i)
                bins, binsIndex = placeItem(itemsCopy[random], bins, binsIndex, binSize)
                itemsCopy.remove(itemsCopy[random])
            # print(f"Elraktuk a {splitNumber * (j+1)}. tárgyig a tárgyakat\n")

    # for bin in bins:
    #     print(str(bin) + "\n")
    # print("\n")
    #
    # print(f"Felhasznált ládák száma: {len(bins)}\n")

    return len(bins)


def FFDBox(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    boxSize = 5

    items.sort(reverse=True, key=itemsSum)

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
    #     print(str(item))
    # print('\n')

    for i in range(len(itemsCopy)):
        if boxSize > len(itemsCopy):
            item = itemsCopy[np.random.random_integers(0, len(itemsCopy)-1)]
            bin, binsIndex = placeItem(item, bins, binsIndex, binSize)
            itemsCopy.remove(item)
        else:
            item = itemsCopy[np.random.random_integers(0, boxSize-1)]
            bin, binsIndex = placeItem(item, bins, binsIndex, binSize)
            itemsCopy.remove(item)

    # for bin in bins:
    #     print(str(bin) + "\n")
    # print("\n")
    #
    # print(f"Felhasznált ládák száma: {len(bins)}\n")
    return len(bins)


def L2NotDet(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    allWeight = []
    boxSize = 5

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    while len(itemsCopy):
        for item in itemsCopy:
            for bin in bins:
                if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (bin.d3FreeCapacity >= item.getD3()):
                    item.itemWeight = pow((int(item.d1) - int(bin.d1FreeCapacity)), 2) + pow((int(item.d2) - int(bin.d2FreeCapacity)), 2) + pow((int(item.d3) - int(bin.d3FreeCapacity)), 2)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
            # print(f"Új ládát kell nyitni! Láda szám: {len(bins)}\n")
            continue
        allWeight.sort(key=itemWeight)

        # for i in allWeight:
        #     print(str(i) + "\n")
        # print("\n")


        if boxSize > len(allWeight):
            randomItemNo = np.random.random_integers(0, len(allWeight)-1)
        else:
            randomItemNo = np.random.random_integers(0, boxSize - 1)

        # print(f"Ezt a tárgyat teszük el: {allWeight[randomItemNo].item}\n")
        bins[int(allWeight[randomItemNo].bin.binIndex - 1)].addItem(allWeight[randomItemNo].item)
        # print(f"Ebbe a ládába tettük a tárgyat: {bins[int(allWeight[randomItemNo].bin.binIndex - 1)]}\n")
        # print("\n")

        itemsCopy.remove(allWeight[randomItemNo].item)
        allWeight.clear()

    # for bin in bins:
    #     print(str(bin) + "\n")
    # print("\n")
    #
    # print(f"Felhasznált ládák száma: {len(bins)}\n")

    return len(bins)


def placeItem(item, bins, binsIndex, binSize):
    # print(str(item) + "\n")
    isItemTaken = False
    # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
    for bin in bins:
        if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (
                bin.d3FreeCapacity >= item.getD3()):
            bin.addItem(item)
            # print(f"A tárgyat elrakjuk a {bin.binIndex} számú ládába!\n")
            # print(str(bin) + "\n")
            # print("\n")
            isItemTaken = True
            break
    # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
    if not isItemTaken:
        binsIndex += 1
        bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
        bins[binsIndex].addItem(item)
        # print(f"Új ládát kell nyitni! Új láda sorszáma: [{len(bins)}]\n")
        # print(f"A tárgyat elrakjuk a {len(bins)} számú ládába!\n")
        # for bin in bins:
        #     print(str(bin) + "\n")
        # print("\n")
    return bins, binsIndex
