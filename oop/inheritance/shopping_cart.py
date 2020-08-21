"""
Take our existing ShoppingCart class.  Create a subclass called
OnlineShoppingCart.  In this case, the "total" method will add
another $10 + 5% of the total for shipping costs.
"""


class ShoppingCart(object):
    def __init__(self):
        self.items = {}

    def add(self, name, price, new_quantity):
        if name in self.items:
            price, previous_quantity = self.items[name]
            self.items[name] = (price, previous_quantity + new_quantity)
        else:
            self.items[name] = (price, new_quantity)

    def total(self):
        total = 0
        return sum([price * quantity for price, quantity in self.items.values()])


class OnlineShoppingCart(ShoppingCart):
    def total(self):
        return super().total()


on = OnlineShoppingCart()
on.add("item1", 5, 2)

print(on.total())
