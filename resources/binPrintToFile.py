def binPrintToFile(bins, file):
    for bin in bins:
        file.write(str(bin) + "\n")
    file.write("\n")