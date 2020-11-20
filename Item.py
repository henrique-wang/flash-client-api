class Item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return ("name: {}; quantity: {}; price: {}".format(self.name, self.quantity, self.price))

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price