import numpy as np


def generateClasses():
    itemdb = [5, 25, 50, 100, 200]  # Hány darab tárgy legyen egy példában

    for i in itemdb:
        # Class1: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 100 és 400 között van
        dataClass("class1", 1000, 1000, 1000, i, 100, 400, 100, 400, 100, 400)
        # Class2: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 1 és 1000 között van
        dataClass("class2", 1000, 1000, 1000, i, 1, 1000, 1, 1000, 1, 1000)
        # Class3: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 200 és 800 között van
        dataClass("class3", 1000, 1000, 1000, i, 200, 800, 200, 800, 200, 800)
        # Class4: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 50 és 200 között van
        dataClass("class4", 1000, 1000, 1000, i, 50, 200, 50, 200, 50, 200)
        # Class5: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 25 és 100 között van
        dataClass("class5", 1000, 1000, 1000, i, 25, 100, 25, 100, 25, 100)
        # a Class4 és 5 esetén az 5 darabosnak nem lesz sok haszna emrt mindig bele dog férni egy ládába, de a többinél jó tesztesetek lehetnek manuális ellenőrzésre

        # Class6: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [1,1/2*LádaMéret][2/3*LádaMéret,LádaMéret][2/3*LádaMéret,LádaMéret]
        # dataClass("class6", 100, 100, 100, i, 1, 50, 66, 100, 66, 100)
        # Class7: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [2/3*LádaMéret,LádaMéret][1,1/2*LádaMéret][2/3*LádaMéret,LádaMéret]
        # dataClass("class7", 100, 100, 100, i, 66, 100, 1, 50, 66, 100)
        # Class8: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [2/3*LádaMéret,LádaMéret][2/3*LádaMéret,LádaMéret][1,1/2*LádaMéret]
        # dataClass("class8", 100, 100, 100, i, 66, 100, 66, 100, 1, 50)
        # Class9: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [1/2*LádaMéret,100][1/2*LádaMéret,LádaMéret][1/2*LádaMéret,LádaMéret]
        # dataClass("class9", 100, 100, 100, i, 50, 100, 50, 100, 50, 100)
        # Class10: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [1,1/2*LádaMéret][1,1/2*LádaMéret][1,1/2*LádaMéret]
        dataClass("class10", 100, 100, 100, i, 1, 50, 1, 50, 1, 50)

        # Class11: Ládák mindegyik dimenziója 40 és a tárgyak mindegyik dimenzióbeli méretei 1 és 10 között van
        dataClass("class11", 10, 10, 10, i, 1, 10, 1, 10, 1, 10)
        # Class12: Ládák mindegyik dimenziója 40 és a tárgyak mindegyik dimenzióbeli méretei 1 és 35 között van
        dataClass("class12", 40, 40, 40, i, 1, 35, 1, 35, 1, 35)


def dataClass(className, b1, b2, b3, i, ws, wl, hs, hl, ds, dl):
    # láda dimenzióinak maximális kapacitása
    b1 = b1
    b2 = b2
    b3 = b3

    r = open("../data/FileNames.txt", "a")
    r.write(f"data\{className}_{i}.txt\n")

    f = open(f"data\{className}_{i}.txt", "w")
    f.write(str(i) + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + " \n")
    for x in range(i):
        w = np.random.random_integers(ws, wl)
        h = np.random.random_integers(hs, hl)
        d = np.random.random_integers(ds, dl)

        f.write(str(x + 1) + " " + str(w) + " " + str(h) + " " + str(d) + " \n")
    r.close()
    f.close()
