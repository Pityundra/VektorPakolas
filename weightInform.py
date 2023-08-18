class WeightInform:
    def __init__(self, item, bin, itemWeight):
        self.item = item
        self.bin = bin
        self.itemWeight = itemWeight

    def __str__(self):
        return f"Súly: [{self.itemWeight}], Tárgy : [{self.item}], Tároló : [{self.bin}]"

    def getItem(self):
        return self.item

    def getBin(self):
        return self.bin


def itemWeight(item):
    return item.itemWeight

