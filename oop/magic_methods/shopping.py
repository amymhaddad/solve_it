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

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        output = []

        for name, info in self.items.items():
            price, quantity = info
            each_item = f"{name:8}: {quantity:3} ${price}"
            output.append(each_item)
        output.append(f"Grand total: {self.total():3}")
        return "\n".join(output)


class OnlineShoppingCart(ShoppingCart):
    def total(self):
        return 1.05 * super().total() + 10


sc = ShoppingCart()
sc.add("pens", 2, 5)
sc.add("cookies", 3, 2)
