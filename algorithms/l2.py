"""
from bin import Bin
from weightInform import WeightInform, itemWeight


def L2(items):
    if len(items) == 0:
        return 0

    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin(binsIndex + 1, 1000, 1000, 1000))  # Itt majd még meg kell csinálni hogy a fileból olvassa be a méretet
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]
    while len(items) > 0:
        for item in items:
            for bin in bins:
                if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (bin.d3FreeCapacity >= item.getD3()):
                    item.itemWeight = pow((int(item.d1)-int(bin.d1FreeCapacity)), 2) + pow((int(item.d2)-int(bin.d2FreeCapacity)), 2) + pow((int(item.d3)-int(bin.d3FreeCapacity)), 2)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin(binsIndex + 1, 1000, 1000, 1000))
            print(f"Új ládát kell nyitni! Láda szám: {len(bins)}\n")
            continue

        allWeight.sort(key=itemWeight)

        for i in allWeight:
            print(i)
        print("\n")

        print(f"Ezt a tárgyat teszük el: {allWeight[0].item}")
        bins[int(allWeight[0].bin.binIndex - 1)].addItem(allWeight[0].item)
        print(f"Ebbe a ládába tettük a tárgyat: {bins[int(allWeight[0].bin.binIndex - 1)]}")
        print("\n")

        items.remove(allWeight[0].item)
        allWeight.clear()

    for bin in bins:
        print(bin)
    print("\n")
    return f"Felhasznált ládák száma: {len(bins)}"
"""
# Kicsit olyan mintha Bin-centrik megvalósítás lenne, de mivel csak akkor nyitunk ládát, amikor már a többibe nem tudunk rakni így mindig csak egy olyan ládánk lesz, amibe tudunk pakolni