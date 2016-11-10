inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# helpers

def add_item(inventory, item_name, item_value=1):
    """ Returns new dict with new added item"""
    if item_name in inventory.keys():
        inventory[item_name] += item_value
    else:
        inventory[item_name] = item_value
    return inventory


def count_values(inventory):
    """ Returns sum of a dictionary's values """
    itemCount = 0
    for item in inventory:
        itemCount += inventory[item]
    return itemCount


def calculate_padding(items):
    """ Returns the length of the longest item in a list """
    maxLength = 0
    for item in items:
        length = len(str(item))
        if length > maxLength:
            maxLength = length
    return maxLength


# main task

def display_inventory(inventory):
    """ Step 1 """
    itemCount = count_values(inventory)
    print("Inventory:")
    for item in inventory:
        print(inventory[item], item)
    print("Total number of items:", itemCount)


def add_to_inventory(inventory, added_items):
    """ Step 2 """
    for item in added_items:
        inventory = add_item(inventory, item)
    return inventory


def print_table(order):
    """ Step 3 """
# Calculating padding
    # min 5 because the length of 'count'
    maxCountLength = max(5, calculate_padding(inv.values()))
    # min 9 because the length of 'item name'
    maxNameLength = max(9, calculate_padding(inv))
# Printing header
    print("Inventory:")
    print("  " + "count".rjust(maxCountLength) + "  " +
          "  " + "item name".rjust(maxNameLength))
    print("-" * (2 + maxCountLength + 2 +
                 2 + maxNameLength))
# Sorting body
    if order == "count,desc":
        sortedKeys = sorted(inv, key=inv.__getitem__, reverse=True)
    elif order == "count,asc":
        sortedKeys = sorted(inv, key=inv.__getitem__, reverse=False)
    else:
        sortedKeys = inv.keys()
# Printing body
    for key in sortedKeys:
        print("  " + str(inv[key]).rjust(maxCountLength) + "  " +
              "  " + str(key).rjust(maxNameLength))
# Printing footer
    print("-" * (2 + maxCountLength + 2 +
                 2 + maxNameLength))
    print("Total number of items:", count_values(inv))


def import_inventory(filename):
    """ Step 4 """
    pass

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
# display_inventory(inv)
print_table("count,desc")
