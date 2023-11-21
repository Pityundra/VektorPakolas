def badExamplesWithOneBigDimension(className, binMax, db):
    r = open("../data/FileNames.txt", "a")
    r.write(f"badExamples\{className}.txt\n")

    f = open(f"badExamples\{className}.txt", "w")
    f.write(str(db) + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + " \n")

    for i in range(db):
        w = np.random.random_integers((2/3)*binMax, binMax)
        h = np.random.random_integers(1, binMax/2)
        d = np.random.random_integers(1, binMax/2)
        # Egy nagy dimenzió és egy kicsi

        rnd = np.random.random_integers(1, 3)
        if rnd == 1:
            f.write(str(w) + " " + str(h) + " " + str(d) + " \n")
        elif rnd == 2:
            f.write(str(h) + " " + str(w) + " " + str(d) + " \n")
        else:
            f.write(str(h) + " " + str(d) + " " + str(w) + " \n")