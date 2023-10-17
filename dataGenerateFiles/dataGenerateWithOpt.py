import numpy


def dataGen():
    dataWithOpt(10, 10, 100, 100, 100)

    dataWithOpt(10, 5, 1000, 1000, 1000)

    dataWithOpt(5, 20, 1000, 1000, 1000)


def dataWithOpt(i, binNumber, bd1, bd2, bd3):
    for y in range(i):
        f = open(f"dataWithOpt\dataWithOpt{binNumber}_test{y + 1}.txt", "w")

        f.write("A ládák dimenziói maximális kapacitása: \n")
        f.write(f"{bd1} {bd2} {bd3}")
        f.write(" \n\n")

        sumItem = 1

        for x in range(binNumber):
            b1 = bd1  # maxitemSize binDimension
            b2 = bd2
            b3 = bd3
            bSum = b1 + b2 + b3
            itemInBin = 0
            while bSum > 0:
                n1 = numpy.random.random_integers(1, b1)
                n2 = numpy.random.random_integers(1, b2)
                n3 = numpy.random.random_integers(1, b3)

                r = numpy.random.random_integers(0, 1)

                # Ha megtelik az egyik dimenzió töltsük fel a többit is
                if b1 - n1 == 0 or b2 - n2 == 0 or b3 - n3 == 0:
                    f.write(str(sumItem) + " " + str(b1) + " " + str(b2) + " " + str(b3) + " \n")
                    bSum = 0
                    itemInBin += 1
                # Utolsó láda ne legyen teljesen feltőltve
                elif x + 1 == binNumber and itemInBin != 0 and r == 1:
                    bSum = 0
                else:
                    f.write(str(sumItem) + " " + str(n1) + " " + str(n2) + " " + str(n3) + " \n")
                    b1 -= n1
                    b2 -= n2
                    b3 -= n3
                    bSum = b1 + b2 + b3
                    itemInBin += 1
                sumItem += 1
            f.write(f"Az {x + 1}. számú ládába {itemInBin} db tárgy került elhelyezésre" + " \n" + " \n")
        f.write(f"Az {sumItem-1} db tárgyat optimálisan {x + 1} ládába tudjuk elpakolni" + " \n" + " \n")

        r = open("../dataWithOpt/FileNames.txt", "a")
        r.write(f"dataWithOpt\dataWithOpt{binNumber}_test{y + 1}.txt\n")
        r.close()
        f.close()
