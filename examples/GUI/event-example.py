# a simple example of an event loop that implements a CLI inventory
# system
#
# requires python 3

import sys

help_str = """
{h, help}                 : show this help
{a, add} item quantity    : add a quantity of item to inventory
{r, remove} item quantity : remove a quantity of item from inventory
{l, list}                 : list the inventory
{q, quit}                 : quit
"""

inventory = {}

while True:

    a = input("\nCommand (or Enter 'h' for help)\n>> ")

    parts = a.split()
    cmd = parts.pop(0)
    
    if cmd in ["h", "help"]:
        print(help_str)

    elif cmd in ["a", "add"]:
        if not len(parts) == 2:
            print("invalid add")
        else:
            if not parts[0] in inventory.keys():
                inventory[parts[0]] = int(parts[1])
            else:
                inventory[parts[0]] += int(parts[1])
            
    elif cmd in ["r", "remove"]:
        if not len(parts) == 2:
            print("invalid remove")
        else:
            if not parts[0] in inventory.keys():
                print("unable to remove -- no items in inventory")
            else:
                inventory[parts[0]] -= int(parts[1])

    elif cmd in ["l", "list"]:
        for k, v in inventory.items():
            print("{:30} {:10}".format(k, v))

    elif cmd in ["q", "quit"]:
        sys.exit()



