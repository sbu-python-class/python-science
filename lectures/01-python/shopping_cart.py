class Item(object):
    """ an item to buy """
    
    def __init__(self, name, quantity=1):
        if name not in INVENTORY:
            raise ValueError
        self.name = name
        self.quantity = quantity
        
    def __repr__(self):
        return "Item({}, {})".format(self.name, self.quantity)
        
    def __eq__(self, other):
        return self.name == other.name
    
    def __add__(self, other):
        if isinstance(other, Item):
            if self == other:
                return(Item(self.name, self.quantity + other.quantity))
            else:
                raise ValueError
        else:
            raise NotImplementedError

            

class ShoppingCart(object):
    
    def __init__(self):
        self.items = []
        
    def subtotal(self):
        """ return a subtotal of our items """
        sub = 0.0
        for i in self.items:
            sub += i.quantity * INVENTORY[i.name]
        return sub

    def add(self, name, quantity):
        """ add an item to our cart """
        item = Item(name, quantity)
        if item in self.items:
            # we already have this, so add to it
            self.items[self.items.index(item)] += item
        else:
            self.items.append(item)
        
    def remove(self, name):
        """ remove all of item name from the cart """
        found = [q for q in self.items if q.name == name]
        if len(found) == 1:
            self.items.remove(found[0])
        
    def report(self):
        for item in self.items:
            print("{:20} : {:4}".format(item.name, item.quantity))
        
