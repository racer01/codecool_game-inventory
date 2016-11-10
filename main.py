inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    itemCount = 0
    print("Inventory:")
    for item in inventory:
        itemCount += inventory[item]
        print(inventory[item], item)
    print("Total number of items:", itemCount)

display_inventory(inv)
