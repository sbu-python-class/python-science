INVENTORY_TEXT = """
apple, 0.60
banana, 0.20
grapefruit, 0.75
grapes, 1.99
kiwi, 0.50
lemon, 0.20
lime, 0.25
mango, 1.50
papaya, 2.95
pineapple, 3.50
blueberries, 1.99
blackberries, 2.50
peach, 0.50
plum, 0.33
clementine, 0.25
cantaloupe, 3.25
pear, 1.25
quince, 0.45
orange, 0.60
"""

# this will be a global -- convention is all caps
INVENTORY = {}
for line in INVENTORY_TEXT.splitlines():
    if line.strip() == "":
        continue
    item, price = line.split(",")
    INVENTORY[item] = float(price)


class Item:
    """ an item to buy """

    def __init__(self, name, quantity=1):
        """keep track of an item that is in our inventory"""
        if name not in INVENTORY:
            raise ValueError("invalid item name")
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}: {self.quantity}"

    def __eq__(self, other):
        """check if the items have the same name"""
        return self.name == other.name

    def __add__(self, other):
        """add two items together if they are the same type"""
        if self.name == other.name:
            return Item(self.name, self.quantity + other.quantity)
        raise ValueError("names don't match")
