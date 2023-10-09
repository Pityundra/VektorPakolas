def itemsSum(item):
    return item.getItemsSum()


def itemsAVG(item):
    return item.getItemsAVG()


def itemsProd(item):
    return item.getItemsProd()


class Item:
    def __init__(self, no, D1, D2, D3):
        self.number = no
        # Dimenziókkénti hely igények
        self.d1 = D1
        self.d2 = D2
        self.d3 = D3

        self.itemsSum = D1 + D2 + D3  # Össz igény
        self.itemsAVG = round((self.d1 + self.d2 + self.d3) / 3, 2)
        self.itemsProd = D1 * D2 * D3
        self.itemWeight = 0

    def __str__(self):
        return f"Tárgy száma: [{self.number}], Dimenziókkénti hely igények: [{self.d1},{self.d2},{self.d3}], Össz igény: [{self.itemsSum}], Igények átlaga: [{self.itemsAVG}], Prod: [{self.itemsProd}]"

    def getNumber(self):
        return self.number

    def getD1(self):
        return self.d1

    def getD2(self):
        return self.d2

    def getD3(self):
        return self.d3

    def getItemsSum(self):
        return self.itemsSum

    def getItemsAVG(self):
        return self.itemsAVG

    def getItemsProd(self):
        return self.itemsProd

    def getItemWeight(self):
        return self.itemWeight
