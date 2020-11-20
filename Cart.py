from Item import Item
class Cart:
    def __init__(self):
        self.product_list = []

    def addItem(self, newItem):
        self.product_list.append(newItem)
        print(len(self.product_list))

    def getTotalPrice(self):
        totalPrice = 0
        for item in self.product_list:
            totalPrice += int(item.quantity) * float(item.price)
        return totalPrice

    def editItem(self, item):
        for curr_item in self.product_list:
            if curr_item.name == item.name:
                curr_item.quantity = item.quantity
                break

    def __str__(self):
        text = ""
        for item in self.product_list:
            if int(item.quantity) > 0:
                text += item.__str__() + "\n"
        text += "Total Price: {}".format(self.getTotalPrice())
        return text