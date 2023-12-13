from resources.bin import Bin
from resources.binPrintToFile import binPrintToFile
from resources.weightInform import WeightInform, itemWeight


def GH(items, alg, binSize, grasp, className):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1


    # r = open(f"results\{className}_Results_Steps.txt", "a")
    # r.write(f"\n{alg}-{grasp}-{className}\n")

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    while len(itemsCopy):
        for item in itemsCopy:
            for bin in bins:
                if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (bin.d3FreeCapacity >= item.getD3()):
                    if alg == "dotP":
                        item.itemWeight = int(item.d1)*int(bin.d1FreeCapacity) + int(item.d2)*int(bin.d2FreeCapacity) + int(item.d3)*int(bin.d3FreeCapacity)
                    elif alg == "L2":
                        item.itemWeight = pow((int(item.d1) - int(bin.d1FreeCapacity)), 2) + pow((int(item.d2) - int(bin.d2FreeCapacity)), 2) + pow((int(item.d3) - int(bin.d3FreeCapacity)), 2)
                    else:
                        return 1
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
            # r.write(f"Új ládát kell nyitni! Láda szám: {len(bins)}\n")
            continue

        if alg == "dotP":
            allWeight.sort(reverse=True, key=itemWeight)
        elif alg == "L2":
            allWeight.sort(key=itemWeight)
        else:
            return 0

        # for i in allWeight:
        #     r.write(str(i) + "\n")
        # r.write("\n")

        if grasp <= len(allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp-1
        else:
            itemChosenNo = len(allWeight)-1

        # r.write(f"Ezt a tárgyat teszük el: {allWeight[itemChosenNo].item}\n")
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # r.write(f"Ebbe a ládába tettük a tárgyat: {bins[int(allWeight[itemChosenNo].bin.binIndex - 1)]}\n")
        # r.write("\n")

        itemsCopy.remove(allWeight[itemChosenNo].item)
        allWeight.clear()

    # binPrintToFile(bins, r)

    # r.write(f"Felhasznált ládák száma: {len(bins)}\n")
    # r.close()

    a_r = open("results\All_Results.txt", "a")
    a_r.write(f"{alg}-{grasp}, {className}, {len(bins)}\n")
    a_r.close()

    return f"{alg} futattva lett a {className}-n!"

# Kicsit olyan mintha Bin-centrik megvalósítás lenne, de mivel csak akkor nyitunk ládát, amikor már a többibe nem tudunk rakni így mindig csak egy olyan ládánk lesz, amibe tudunk pakolni