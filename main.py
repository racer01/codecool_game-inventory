inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    """ Step 1 """
    itemCount = 0
    print("Inventory:")
    for item in inventory:
        itemCount += inventory[item]
        print(inventory[item], item)
    print("Total number of items:", itemCount)


def add_to_inventory(inventory, added_items):
    """ Step 2 """
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
