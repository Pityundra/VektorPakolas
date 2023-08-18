from bin import Bin
from item import itemsSum, itemsAVG


def FFD(items, centric, SA, binSize, className):
    if centric == "item":
        return FFDIC(items, SA, binSize, className)
    elif centric == "bin":
        return FFDBC(items, SA, binSize, className)
    else:
        print("Nem bin vagy item!")
        return 1


# FFD Item-Centric
def FFDIC(items, SA, binSize, className):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    r = open(f"results\{className}_Results_Steps.txt", "a")
    r.write(f"\nFFD-IC-{SA}-{className}\n")

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    if SA == "sum":
        # A kapott tárgyakat a dimenziói összege alapján csökkenő sorrendbe tesszük
        itemsCopy.sort(reverse=True, key=itemsSum)
    elif SA == "avg":
        itemsCopy.sort(reverse=True, key=itemsAVG)
    else:
        print("Nem sum vagy avg!")
        return 1

    for item in itemsCopy:
        r.write(str(item) + "\n")
    r.write("\n")
    bins = []   # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex+1, binSize[0], binSize[1], binSize[2]))

    for item in itemsCopy:
        r.write(str(item) + "\n")
        isItemTaken = False
        # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
        for bin in bins:
            # print(bin.d1FreeCapacity, bin.d2FreeCapacity, bin.d3FreeCapacity)
            if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (bin.d3FreeCapacity >= item.getD3()):
                bin.addItem(item)
                r.write(f"A tárgyat elrakjuk a {bin.binIndex} számú ládába!\n")
                isItemTaken = True
                for bin in bins:
                    r.write(str(bin) + "\n")
                r.write("\n")
                break
        # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
        if not isItemTaken:
            binsIndex += 1
            bins.append(Bin(binsIndex+1, binSize[0], binSize[1], binSize[2]))
            bins[binsIndex].addItem(item)
            r.write(f"Új ládát kell nyitni! Új láda sorszáma: [{len(bins)}]\n")
            for bin in bins:
                r.write(str(bin) + "\n")
            r.write("\n")
    r.write(f"Felhasznált ládák száma: {len(bins)}\n")
    r.close()

    a_r = open("results\All_Results.txt", "a")
    a_r.write(f"FFD-IC-{SA}, {className}, {len(bins)}\n")
    a_r.close()

    return f"Az FFD-IC-{SA} futattva lett a {className}-n!"


# FFD Bin-Centric
def FFDBC(items, SA, binSize, className):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    r = open(f"results\{className}_Results_Steps.txt", "a")
    r.write(f"\nFFD-BC-{SA}-{className}\n")

    itemsCopy = []
    itemsCopy2 = []
    for item in items:
        itemsCopy.append(item)
        itemsCopy2.append(item)
        r.write(str(item) + "\n")
    r.write("\n")

    if SA == "sum":
        # A kapott tárgyakat a dimenziói összege alapján csökkenő sorrendbe tesszük
        itemsCopy.sort(reverse=True, key=itemsSum)
    elif SA == "avg":
        itemsCopy.sort(reverse=True, key=itemsAVG)
    else:
        return 1

    bins = []   # Felhasznált ládák listája
    openBinIndex = 0  # A ládák indexelésére

    while len(itemsCopy2) > 0:
        # r.write(str(len(itemsCopy)))
        bins.append(Bin(openBinIndex + 1, binSize[0], binSize[1], binSize[2]))
        for item in itemsCopy:
            # Ha belefér egy item a nyitott ládába akkor beleteszi és kiveszi a listából
            if item in itemsCopy2 and (bins[openBinIndex].d1FreeCapacity >= item.getD1()) and (bins[openBinIndex].d2FreeCapacity >= item.getD2()) and (bins[openBinIndex].d3FreeCapacity >= item.getD3()):
                r.write(str(item) + "\n")
                bins[openBinIndex].addItem(item)
                r.write(f"A [{item.getNumber()}] tárgyat elrakjuk a {bins[openBinIndex].binIndex} számú nyitott ládába!\n")
                r.write(f"Nyitott láda: {bins[openBinIndex]} \n")
                itemsCopy2.remove(item)
        openBinIndex += 1

    r.write("\n")
    for bin in bins:
        r.write(str(bin) + "\n")
    r.write("\n")

    r.write(f"Felhasznált ládák száma: {len(bins)}\n")
    r.close()

    a_r = open("results\All_Results.txt", "a")
    a_r.write(f"FFD-BC-{SA}, {className}, {len(bins)}\n")
    a_r.close()

    return f"Az FFD-BC-{SA} futattva lett a {className}-n!"