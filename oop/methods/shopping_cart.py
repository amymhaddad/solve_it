"""
Create a ShoppingCart class.

sc = ShoppingCart()
sc.add('book', 30, 1)    # name, price-per-unit, quantity
sc.add('toothbrush', 3, 4)

sc.remove('toothbrush')   # removes one toothbrush -- or removes
                            # the item altogether if the quantity is 0

sc.total()  # returns the total price of items in the shopping cart
"""


class ShoppingCart(object):
    # Need __init__ to store stuff
    def __init__(self):
        self.items = []

    def add(self, name, price, quantity):
        if not self.items:
            item = {"name": name, "price": price, "quantity": quantity}
            self.items.append(item)

        for item in self.items:
            if item["name"] == name:
                item["quantity"] += quantity

    def remove(self, name):
        for item in self.items:
            if item["name"] == name and item["quantity"] == 0:
                self.items.remove(item)
            item["quantity"] -= 1
        return self.items

    def total(self):
        total = 0
        for item in self.items:
            if item["price"]:
                total += float(item["price"]) * int(item["quantity"])
        return total


sc = ShoppingCart()
sc.add("book1", 30, 1)
sc.add("book1", 30, 2)
sc.add("book3", 30, 2)

print(sc.items)

