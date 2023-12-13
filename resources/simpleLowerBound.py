from math import ceil


def SimpleLowerBound(items, binSize, className):
    d1Sum = 0
    d2Sum = 0
    d3Sum = 0

    for item in items:
        d1Sum += item.getD1()
        d2Sum += item.getD2()
        d3Sum += item.getD3()

    lowerBound = max(ceil(d1Sum/binSize[0]), ceil(d3Sum/binSize[1]), ceil(d3Sum/binSize[2]))

    if className:
        r = open(f"results\{className}_Results_Steps.txt", "a")
        r.write("Az osztályra számolt egyszerű alsó korlát: " + str(lowerBound) + "\n")
        r.close()

    # print(f"A {className} inputon legalább {lowerBound} db láda fog kelleni!")
    """
    Ez ugye azt nem veszi figyelembe ha a tárgyakat nem lehet egymás mellé pakolni így azokban az esetekben
    amikor mindegyik elemet külön kell tegyünk nagyon távoli korlátott add, pedig nem lehet jobb pakolást összehozni
    sehogy semm.
    """

    return lowerBound