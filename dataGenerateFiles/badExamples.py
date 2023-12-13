import numpy as np


def badExamplesgen():
    itemdb = [100, 200, 400, 800, 1000]
    for i in itemdb:
        badExamplesWithOneBigDimension(f"bad_{i}_item", 1000, i)


def badExamplesWithOneBigDimension(className, binMax, db):
    r = open("badExamples/FileNames.txt", "a")
    r.write(f"badExamples\{className}.txt\n")

    f = open(f"badExamples\{className}.txt", "w")
    f.write(str(db) + " \n")
    f.write(str(binMax) + " " + str(binMax) + " " + str(binMax) + " " + " \n")

    for i in range(db):
        w = np.random.random_integers((2/3)*binMax, binMax)
        h = np.random.random_integers(1, binMax/2)
        d = np.random.random_integers(1, binMax/2)
        # Egy nagy dimenzió és kettő kicsi

        rnd = np.random.random_integers(1, 3)
        if rnd == 1:
            f.write(str(i+1) + " " + str(w) + " " + str(h) + " " + str(d) + " \n")
        elif rnd == 2:
            f.write(str(i+1) + " " + str(h) + " " + str(w) + " " + str(d) + " \n")
        else:
            f.write(str(i+1) + " " + str(h) + " " + str(d) + " " + str(w) + " \n")


def badExamplesEpsilon():
    r = open("badExamples\FileNames.txt", "a")
    r.write(f"badExamples\epsilon.txt\n")

    f = open(f"badExamples\epsilon.txt", "w")
    f.write(str(30) + " \n")
    f.write("999 " + " 999 " + "999 \n")

    for i in range(10):
        f.write(str(i+1) + " " "334 " + "333 " + "332 \n")
    for i in range(11, 21):
        f.write(str(i) + " " + "332 " + "334 " + "333 \n")
    for i in range(21, 31):
        f.write(str(i) + " " + "333 " + "332 " + "334 \n")

